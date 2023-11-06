from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from djoser.email import ActivationEmail



class MyActivationEmail(ActivationEmail):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_name = 'social/activation.html'

    def send(self, to, *args, **kwargs):
        context = self.get_context_data()
        subject = 'Account activation on Iatsun Social'  # Set your custom subject here
        body = render_to_string(self.template_name, context)
        text_body = strip_tags(body)

        email_message = EmailMultiAlternatives(subject, text_body, to=to)
        email_message.attach_alternative(body, "text/html")
        email_message.send()

    def get_context_data(self):
        context = super().get_context_data()
        context['protocol'] = settings.EMAIL_PROTOCOL
        context['domain'] = settings.EMAIL_DOMAIN
        return context
