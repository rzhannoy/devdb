# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'email_confirmed', 'date_joined']


admin.site.register(User, UserAdmin)
