from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication, MultiAuthentication

from project.resources import BaseResource, DEFAULT_ALLOWED
from project.auth import AnyReadAuthentication

from core.models import Cv
from .auth import CvAuthorization


class CvResource(BaseResource):
    user = fields.ToOneField('users.api.UserResource', 'user', full=False)
    skill_groups = fields.ToManyField('core.api.SkillGroupResource', 'skill_groups', full=True, full_list=False, null=True)
    projects = fields.ToManyField('core.api.ProjectResource', 'projects', full=True, full_list=False, null=True)
    links = fields.ToManyField('core.api.LinkResource', 'links', full=True, full_list=False, null=True)

    class Meta:
        queryset = Cv.objects.all()
        allowed_methods = []
        resource_name = 'cv'
        authentication = MultiAuthentication(AnyReadAuthentication(), ApiKeyAuthentication())
        authorization = CvAuthorization()
