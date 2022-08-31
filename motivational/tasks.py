from celery import shared_task

from django.core.mail import send_mail
from .models.motivational_message import MotivationalMessage

@shared_task(bind=True)
def sendEmail(self, pk):
    notification = MotivationalMessage.objects.get(id=pk)
    subject = notification.title
    content = notification.content
    send_mail(subject, content, 'wilferfonseca@outlook.com', ['faxobo5905@lurenwu.com'], fail_silently=False)
