from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized


class BaseAuthorization(Authorization):
    def reject(self):
        raise Unauthorized('permission_rejected')

    def read_list(self, object_list, bundle):
        self.reject()

    def read_detail(self, object_list, bundle):
        self.reject()

    def create_list(self, object_list, bundle):
        self.reject()

    def create_detail(self, object_list, bundle):
        self.reject()

    def update_list(self, object_list, bundle):
        self.reject()

    def update_detail(self, object_list, bundle):
        self.reject()

    def delete_list(self, object_list, bundle):
        self.reject()

    def delete_detail(self, object_list, bundle):
        self.reject()


class AnyReadAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        return False

    def get_identifier(self, request):
        return request.user.email
