from tastypie.api import Api

from users.api import UserResource
from core.api import CvResource, SkillGroupResource, SkillResource
from core.api import ProjectResource, LinkResource, MessageResource


api = Api(api_name='api')

api.register(UserResource())
api.register(CvResource())
api.register(SkillGroupResource())
api.register(SkillResource())
api.register(ProjectResource())
api.register(LinkResource())
api.register(MessageResource())
