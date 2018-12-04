from project.auth import BaseAuthorization


class UserAuthorization(BaseAuthorization):
    def read_detail(self, object_list, bundle):
        return True

    def update_detail(self, object_list, bundle):
        if bundle.obj.id == bundle.request.user.id:
            return True

        self.reject()
