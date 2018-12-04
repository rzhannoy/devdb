from django.conf.urls import url, include
from django.contrib import admin

from .api import api


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(api.urls)),
]
