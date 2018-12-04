from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication

from project.resources import BaseResource, ALL_ALLOWED

from core.models import Link
from .auth import CvChildAuthorization


class LinkResource(BaseResource):
    cv = fields.ToOneField('core.api.CvResource', 'cv', full=False)

    class Meta:
        queryset = Link.objects.all()
        allowed_methods = ALL_ALLOWED
        resource_name = 'link'
        authentication = ApiKeyAuthentication()
        authorization = CvChildAuthorization()
