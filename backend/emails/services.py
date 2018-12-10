# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .tasks import send_email as send_email_async


class Mailer(object):
    def send_email(self, email):
        send_email_async.delay(email)

    def send_test(self):
        msg = EmailMultiAlternatives(
            'From DevDB to Nick Ten',
            'Hello, Nick Ten. Please confirm your email. Regards, @devdb',
            settings.DEFAULT_FROM_EMAIL,
            ['nrzhannoy@gmail.com']
        )

        self.send_email(msg)

    def send_registration_email(self, user):
        subject = 'Get started with DevDB'
        body = render_to_string('emails/registration.txt', {
            'name': user.gen_name(),
            'link': user.gen_confirmation_link(),
        })

        email = EmailMultiAlternatives(
            subject, body, settings.DEFAULT_FROM_EMAIL, [user.email]
        )

        self.send_email(email)

    def send_cv_message(self, message):
        subject = 'DevDB: You received a new message'
        body = render_to_string('emails/cv_message.txt', {
            'name': message.to.gen_name(),
            'message': message.message,
        })

        email = EmailMultiAlternatives(
            subject, body, settings.DEFAULT_FROM_EMAIL, [message.to.email]
        )

        self.send_email(email)
