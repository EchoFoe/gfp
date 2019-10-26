from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from gfp.settings import FROM_EMAIL, EMAIL_ADMIN
from emails.models import EmailSendingFact
from django.forms.models import model_to_dict


class SendingEmail(object):
    from_email = "GFP <%s>" % FROM_EMAIL
    reply_to_emails = [from_email]
    target_emails = []
    bcc_emails = []

    def sending_email(self, type_id, email=None, order=None):
        global subject, message
        if not email:
            email = EMAIL_ADMIN
        target_emails = [email]

        vars = dict()
        if type_id == 1:
            subject = "Новая заявка"
            vars["order"] = order
            subject = 'Клиент подал заявку на участие в турнире!'
            message = get_template('emails_templates/notification_admin.html').render(vars)

        elif type_id == 2:
            subject = 'Ваша заявка получена!'
            vars["order"] = order
            message = get_template('emails_templates/notification_customer.html').render(vars)

        msg = EmailMessage(subject, message, from_email=self.from_email, to=target_emails, bcc=self.bcc_emails, reply_to=self.reply_to_emails)
        msg.content_subtype = 'html'
        msg.mixed_subtype = 'related'
        msg.send()

        kwargs = {
            "type_id": type_id,
            "email": email
        }
        if order:
            kwargs["sportsman"] = order
        EmailSendingFact.objects.create(**kwargs)