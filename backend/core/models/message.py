# pylint: disable=E1136
from django.db import models
from project.base_models import Model
from emails.services import Mailer


mailer = Mailer()


class Message(Model):
    to = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='messages')

    message = models.CharField(max_length=500)

    def __unicode__(self):
        return self.message[:25]

    def send(self):
        mailer.send_cv_message(self)
