from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication

from project.resources import BaseResource, ALL_ALLOWED

from core.models import SkillGroup
from .auth import CvChildAuthorization


class SkillGroupResource(BaseResource):
    cv = fields.ToOneField('core.api.CvResource', 'cv', full=False)
    skills = fields.ToManyField('core.api.SkillResource', 'skills', full=True, full_list=False, null=True)

    class Meta:
        queryset = SkillGroup.objects.all()
        allowed_methods = ALL_ALLOWED
        resource_name = 'skill-group'
        authentication = ApiKeyAuthentication()
        authorization = CvChildAuthorization()

    def save(self, bundle, skip_errors=False):
        skills = None
        if not bundle.obj.id:
            skills = bundle.data.pop('skills', None)

        bundle = super(SkillGroupResource, self).save(bundle, skip_errors=False)

        if skills:
            group_resource_uri = self.get_resource_uri(bundle)

            for skill in skills:
                skill['group'] = group_resource_uri

            bundle.data['skills'] = skills
            skills = None

            bundle = super(SkillGroupResource, self).save(bundle, skip_errors=False)

        return bundle
