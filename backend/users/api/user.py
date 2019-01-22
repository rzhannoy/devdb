from django.conf.urls import url
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from django.db.models import Max

from tastypie import fields
from tastypie import http
from tastypie.authentication import ApiKeyAuthentication, MultiAuthentication
from tastypie.utils import trailing_slash

from project.resources import BaseResource, DEFAULT_ALLOWED
from project.auth import AnyReadAuthentication

from users.models import User
from core.models import Skill

from .auth import UserAuthorization


class UserResource(BaseResource):
    cv = fields.ToOneField('core.api.CvResource', 'cv', full=True)

    extra_data = fields.DictField('extra_data', blank=True)

    class Meta:
        queryset = User.objects.filter(is_active=True)
        allowed_methods = DEFAULT_ALLOWED
        resource_name = 'user'
        detail_uri_name = 'handle'
        always_return_data = True
        authentication = MultiAuthentication(AnyReadAuthentication(), ApiKeyAuthentication())
        authorization = UserAuthorization()

        excludes = [
            'is_staff', 'is_superuser',
            'password', 'token',
            'is_active', 'confirmation_code',
            'email',
        ]

    def prepend_urls(self):
        return [
            url(r'^(?P<resource_name>{})/register{}$'.format(self._meta.resource_name, trailing_slash()), self.wrap_view('register'), name='api_register'),
            url(r'^(?P<resource_name>{})/confirm{}$'.format(self._meta.resource_name, trailing_slash()), self.wrap_view('confirm'), name='api_confirm'),
            url(r'^(?P<resource_name>{})/login{}$'.format(self._meta.resource_name, trailing_slash()), self.wrap_view('login'), name='api_login'),
            url(r'^(?P<resource_name>{})/logout{}$'.format(self._meta.resource_name, trailing_slash()), self.wrap_view('logout'), name='api_logout'),
            url(r'^(?P<resource_name>{})/change-password{}$'.format(self._meta.resource_name, trailing_slash()), self.wrap_view('change_password'), name='api_change_password'),
            url(r'^(?P<resource_name>{})/delete{}$'.format(self._meta.resource_name, trailing_slash()), self.wrap_view('handle_delete'), name='api_handle_delete'),
            url(r'^(?P<resource_name>{})/count{}$'.format(self._meta.resource_name, trailing_slash()), self.wrap_view('gen_count'), name='api_gen_count'),

            url(r'^(?P<resource_name>{})/(?P<handle>.+){}$'.format(self._meta.resource_name, trailing_slash()), self.wrap_view('dispatch_detail'), name='api_dispatch_detail'),
        ]

    def save(self, bundle, skip_errors=False):
        bundle = super(UserResource, self).save(bundle, skip_errors=False)

        group_ids = list(bundle.obj.cv.skill_groups.values_list('id', flat=True))
        if group_ids:
            level_max = Skill.objects.filter(
                group_id__in=group_ids
            ).aggregate(Max('level'))['level__max']

            bundle.obj.show_skills_legend = level_max > 0
            bundle.obj.save()

        return bundle

    def _create_auth_response(self, request, user):
        user_data = self.serialize_obj(request, user,
            extra_data={'token': user.token}
        )

        return self.create_response(request, {
            'success': True,
            'user': user_data,
        })

    def register(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        data = self.deserialize(request, request.body)
        data['handle'] = slugify(data['handle'])
        validation = User.validate(data)

        if not validation['is_valid']:
            return self.create_error_response(request, validation)

        user = User.register(data)

        return self._create_auth_response(request, user)

    def confirm(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        data = self.deserialize(request, request.body)

        user = get_object_or_404(User, email=data['email'])
        success = user.confirm(data['confirmation_token'])

        if not success:
            return self.create_error_response(request, 'token_invalid')

        return self._create_auth_response(request, user)

    def login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        data = self.deserialize(request, request.body)

        user = authenticate(
            email=data.get('email'),
            password=data.get('password')
        )

        if user and user.is_active:
            return self._create_auth_response(request, user)

        return self.create_error_response(request, 'credentials_invalid', http.HttpUnauthorized)

    def change_password(self, request, **kwargs):
        self.process_request(request)

        user = request.user
        data = self.deserialize(request, request.body)

        if not user.check_password(data['old_password']):
            return self.create_error_response(request, 'incorrect_password')

        user.set_password(data['new_password'])
        user.save()

        return self.create_response(request, {'success': True})

    def handle_delete(self, request, **kwargs):
        self.process_request(request)

        user = request.user
        data = self.deserialize(request, request.body)

        if not user.check_password(data['password']):
            return self.create_error_response(request, 'incorrect_password')

        user.delete()

        return self.create_response(request, {'success': True})

    def gen_count(self, request, **kwargs):
        self.process_request(request, ['get'])

        return self.create_response(request, {
            'success': True,
            'count': User.objects.count(),
        })
