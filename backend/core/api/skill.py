from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication

from project.resources import BaseResource, ALL_ALLOWED

from core.models import Skill
from .auth import SkillAuthorization


class SkillResource(BaseResource):
    group = fields.ToOneField('core.api.SkillGroupResource', 'group', full=False)

    class Meta:
        queryset = Skill.objects.all()
        allowed_methods = ALL_ALLOWED
        resource_name = 'skill'
        authentication = ApiKeyAuthentication()
        authorization = SkillAuthorization()
