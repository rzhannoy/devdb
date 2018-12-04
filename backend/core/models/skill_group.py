from django.db import models
from project.base_models import Model


class SkillGroup(Model):
    cv = models.ForeignKey('core.Cv', on_delete=models.CASCADE, related_name='skill_groups')

    title = models.CharField(max_length=100, blank=True)
    position = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        return self.title or u'skill group #{}'.format(self.id)
