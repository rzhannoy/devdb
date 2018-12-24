from tastypie.api import Api as TastypieApi
from tastypie.http import HttpForbidden

from users.api import UserResource
from core.api import CvResource, SkillGroupResource, SkillResource
from core.api import ProjectResource, LinkResource, MessageResource


class Api(TastypieApi):
    def top_level(self, request, api_name=None):
        return HttpForbidden()


api = Api(api_name='api')

api.register(UserResource())
api.register(CvResource())
api.register(SkillGroupResource())
api.register(SkillResource())
api.register(ProjectResource())
api.register(LinkResource())
api.register(MessageResource())
