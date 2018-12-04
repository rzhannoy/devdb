from django.db import models
from project.base_models import Model


class Link(Model):
    cv = models.ForeignKey('core.Cv', on_delete=models.CASCADE, related_name='links')

    title = models.CharField(max_length=100, blank=True)
    position = models.PositiveSmallIntegerField(null=True, blank=True)
    url = models.CharField(max_length=1000, blank=True)

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        return self.title or u'link #{}'.format(self.id)
