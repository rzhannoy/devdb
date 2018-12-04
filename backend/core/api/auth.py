from project.auth import BaseAuthorization


class CvAuthorization(BaseAuthorization):
    def read_detail(self, object_list, bundle):
        return True

    def update_detail(self, object_list, bundle):
        if bundle.obj.user_id == bundle.request.user.id:
            return True

        self.reject()


class CvChildAuthorization(BaseAuthorization):
    def user_check_local(self, bundle):
        self.user_check(bundle, bundle.obj.cv.user_id)

    def read_detail(self, object_list, bundle):
        return True

    def read_list(self, object_list, bundle):
        return object_list

    def update_detail(self, object_list, bundle):
        self.user_check_local(bundle)

    def create_detail(self, object_list, bundle):
        self.user_check_local(bundle)

    def delete_detail(self, object_list, bundle):
        self.user_check_local(bundle)


class SkillAuthorization(BaseAuthorization):
    def user_check_local(self, bundle):
        self.user_check(bundle, bundle.obj.group.cv.user_id)

    def read_detail(self, object_list, bundle):
        return True

    def read_list(self, object_list, bundle):
        return object_list

    def update_detail(self, object_list, bundle):
        self.user_check_local(bundle)

    def create_detail(self, object_list, bundle):
        self.user_check_local(bundle)

    def delete_detail(self, object_list, bundle):
        self.user_check_local(bundle)
