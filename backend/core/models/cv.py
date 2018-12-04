from django.db import models

from project.base_models import Model
from project.mixins import HtmlFieldsMixin


class CvManager(models.Manager):
    def prefetched(self):
        return self.select_related('user').prefetch_related(
            'skill_groups__skills',
            'projects',
            'links',
        )


class Cv(HtmlFieldsMixin, Model):
    DONT_DISPLAY = 'dd'

    REMOTE_READY = 'rr'
    REMOTE_ONLY = 'ro'
    NO_REMOTE = 'nr'

    REMOTE_CHOICES = (
        (DONT_DISPLAY, 'Don\'t display'),
        (REMOTE_READY, 'Remote-ready'),
        (REMOTE_ONLY, 'Remote-only'),
        (NO_REMOTE, 'No remote'),
    )

    RELOCATION_READY = 'rr'
    NO_RELOCATION = 'nr'

    RELOCATION_CHOICES = (
        (DONT_DISPLAY, 'Don\'t display'),
        (RELOCATION_READY, 'Relocation-ready'),
        (NO_RELOCATION, 'No relocation'),
    )

    MALE = 'ma'
    FEMALE = 'fe'
    TRANS = 'tr'

    GENDER_CHOICES = (
        (DONT_DISPLAY, 'Don\'t display'),
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (TRANS, 'Trans*'),
    )

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    specialty = models.CharField(max_length=100, blank=True)
    remote = models.CharField(max_length=2, choices=REMOTE_CHOICES, default=DONT_DISPLAY)
    relocation = models.CharField(max_length=2, choices=RELOCATION_CHOICES, default=DONT_DISPLAY)
    city = models.CharField(max_length=100, blank=True)
    languages = models.CharField(max_length=100, blank=True)
    timezone = models.CharField(max_length=100, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=DONT_DISPLAY)
    introduction = models.TextField(blank=True)
    willing_to_try = models.TextField(blank=True)
    other_details = models.TextField(blank=True)

    objects = CvManager()

    def __unicode__(self):
        return u'cv for user #{}'.format(self.user_id)

    @property
    def html_fields(self):
        return ['introduction', 'other_details']
