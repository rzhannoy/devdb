# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


class CvAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'updated']


class SkillAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'position']


class SkillGroupAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'position']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'position']


class LinkAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'position']


admin.site.register(Cv, CvAdmin)
admin.site.register(SkillGroup, SkillGroupAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Message)
