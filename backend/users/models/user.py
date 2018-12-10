from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin, AbstractBaseUser, BaseUserManager
)
from django.db.models import signals
from django.contrib.postgres.fields import JSONField

from tastypie.models import create_api_key

from project.utils import gen_random_string

from emails.services import Mailer

from core.models import Cv


mailer = Mailer()


################
##  MANAGERS  ##
################

class UserManager(BaseUserManager):
    def create_user(self, email, handle, password=None, **extra_fields):
        user = self.model(email=email, handle=handle, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        user.denormalize_token()

        return user

    def create_superuser(self, email, handle, password, **extra_fields):
        user = self.create_user(email, handle, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.email_confirmed = True
        user.save(using=self._db)

        return user


##############
##  MODELS  ##
##############

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    handle = models.CharField(max_length=120, unique=True)
    confirmation_code = models.CharField(max_length=40)
    token = models.CharField(max_length=300, blank=True)

    extra_data = JSONField(default=dict, blank=True)

    date_joined = models.DateTimeField(auto_now_add=True)

    email_confirmed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['handle']

    class Meta:
        ordering = ['-date_joined']

    def __unicode__(self):
        return u'{}'.format(self.email)

    def save(self, *args, **kwargs):
        if not self.confirmation_code:
            self.confirmation_code = gen_random_string()

        return super(User, self).save(*args, **kwargs)

    @staticmethod
    def validate(data):
        result = {}

        if User.objects.filter(email=data['email']).exists():
            result['email_exists'] = True

        if User.objects.filter(handle=data['handle']).exists():
            result['handle_exists'] = True

        if len(data['handle']) < settings.USER_HANDLE_LIMIT:
            result['handle_length'] = True

        if not data.get('password'):
            result['password_required'] = True

        result['is_valid'] = True if not result else False

        return result

    @staticmethod
    def register(data):
        user = User.objects.create_user(**data)
        Cv.objects.create(user=user)
        mailer.send_registration_email(user)

        return user

    def gen_confirmation_link(self):
        return '{}?email={}&confirmation_token={}'.format(
            settings.FRONTEND_URL,
            self.email,
            self.confirmation_code
        )

    def confirm(self, token):
        if self.confirmation_code == token:
            self.email_confirmed = True
            self.save()
            return True

        return False

    def get_short_name(self):
        return u'{}'.format(self.first_name)

    def get_full_name(self):
        return u'{} {}'.format(self.first_name, self.last_name)

    def gen_name(self):
        return self.first_name if self.first_name else self.handle

    def denormalize_token(self):
        self.token = '{}:{}'.format(self.email, self.api_key.key)
        self.save()

signals.post_save.connect(create_api_key, sender=User)
