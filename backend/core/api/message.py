from tastypie import fields
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization

from project.resources import BaseResource, DEFAULT_ALLOWED

from core.models import Message


class MessageResource(BaseResource):
    to = fields.ToOneField('users.api.UserResource', 'to', full=False, null=True)
    to_id = fields.IntegerField('to_id')

    class Meta:
        queryset = Message.objects.all()
        allowed_methods = DEFAULT_ALLOWED
        resource_name = 'message'
        authentication = Authentication()
        authorization = Authorization()
