from tastypie import http
from tastypie.resources import ModelResource


DEFAULT_ALLOWED = ['get', 'post', 'put', 'patch']
READ_ALLOWED = ['get']
ALL_ALLOWED = ['options', 'get', 'post', 'put', 'patch', 'delete']


class BaseResource(ModelResource):
    # def full_dehydrate(self, bundle, for_list=False):
    #     bundle = super(BaseResource, self).full_dehydrate(bundle, for_list)

    #     self.handle_file_fields(bundle)

    #     return bundle

    def deserialize(self, request, data, format=None):
        '''
        Supports multipart/form-data POST requests
        '''
        if not format:
            format = request.META.get('CONTENT_TYPE', 'application/json')

        if format == 'application/x-www-form-urlencoded':
            return request.POST

        if format.startswith('multipart'):
            data = request.POST.copy()
            data.update(request.FILES)

            return data

        return super(BaseResource, self).deserialize(request, data, format)

    def create_error_response(self, request, message=None, response_class=http.HttpBadRequest):
        response = {'success': False}
        if message:
            response['message'] = message

        return self.create_response(request, response, response_class)

    def process_request(self, request, allowed=['post']):
        self.method_check(request, allowed=allowed)
        self.is_authenticated(request)

    def serialize_obj(self, request, obj, extra_data=None, **kwargs):
        bundle = self.build_bundle(obj=obj, request=request)

        if extra_data:
            bundle.data.update(extra_data)

        serialized = self.full_dehydrate(bundle, **kwargs)

        return serialized

    def serialize_collection(self, request, collection):
        serialized = []
        for obj in collection:
            serialized.append(self.serialize_obj(request, obj, for_list=True))

        return serialized

    @property
    def model_class(self):
        return self._meta.object_class.__name__

    # def handle_file_fields(self, bundle):
    #     file_fields = getattr(self._meta, 'file_fields', None)

    #     if file_fields:
    #         for field in file_fields:
    #             bundle.data[field] = getattr(bundle.obj, field)
