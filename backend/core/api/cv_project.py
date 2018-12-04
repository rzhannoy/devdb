from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication

from project.resources import BaseResource, ALL_ALLOWED

from core.models import Project
from .auth import CvChildAuthorization


class ProjectResource(BaseResource):
    cv = fields.ToOneField('core.api.CvResource', 'cv', full=False)

    class Meta:
        queryset = Project.objects.all()
        allowed_methods = ALL_ALLOWED
        resource_name = 'project'
        authentication = ApiKeyAuthentication()
        authorization = CvChildAuthorization()
