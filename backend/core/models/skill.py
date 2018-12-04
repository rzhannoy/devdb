from django.db import models
from project.base_models import Model


class Skill(Model):
    group = models.ForeignKey('core.SkillGroup', on_delete=models.CASCADE, related_name='skills')

    title = models.CharField(max_length=100, blank=True)
    position = models.PositiveSmallIntegerField(null=True, blank=True)
    level = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        return self.title or u'skill #{}'.format(self.id)
