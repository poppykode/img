import datetime
import smtplib
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_notification_mail(to, message, subject):
    try:
        today = datetime.date.today()
        formatted_date = today.strftime("%A %d %B, %Y")
        message_html = get_template("email/general.html").render(
            {"subject": subject, "message": message, "date": formatted_date}
        )
        send_mail(
            subject=subject, 
            message='',
            html_message=message_html,
            recipient_list=[to],
            from_email="expresscareweb@gmail.com",
            fail_silently=False)
    except smtplib.SMTPRecipientsRefused as err:
        print(err)
