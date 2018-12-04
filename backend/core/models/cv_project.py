from django.db import models

from project.base_models import Model
from project.mixins import HtmlFieldsMixin


class Project(HtmlFieldsMixin, Model):
    cv = models.ForeignKey('core.Cv', on_delete=models.CASCADE, related_name='projects')

    title = models.CharField(max_length=100, blank=True)
    position = models.PositiveSmallIntegerField(null=True, blank=True, default=1)
    tag = models.CharField(max_length=20, blank=True)
    website = models.CharField(max_length=1000, blank=True)
    role = models.CharField(max_length=100, blank=True)
    stack = models.TextField(blank=True)
    scope = models.TextField(blank=True)

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        return self.title or u'project #{}'.format(self.id)

    @property
    def html_fields(self):
        return ['stack', 'scope']
