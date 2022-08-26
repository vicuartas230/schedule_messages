from __future__ import absolute_import, unicode_literals
from celery import task

#imports needed for the functions
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
# from .models import *
from django.contrib.auth.models import User
from .models.motivational_message import MotivationalMessage


def sendEmail(email, subject, to_email):
    #Logic to send an email here ........
    @task()
    def scheduledTask():
    #Get Subscriptions
        notifications = MotivationalMessage.objects.all()
        for nx in notifications:
            if nx.is_active:
                selection = nx.subscribed_category

notification = MotivationalMessage.objects.get(id=1)
jobs = Jobs.objects.filter(company=the_company, category__title__contains=selection)[:3]

subject = 'Weekly Notifications'

email_jobs = {
    "title": "Job Notifications from Careers Portal",
    "shortDescription": "Thank you for subscribing to Careers Portal, job notifications. For more jobs visit https://careers-portal.co.za",
    "subtitle": "Careers Portal - The latest job opportunities, updated weekly",
    "jobs": jobs
}

sendEmail(email_jobs, subject, [nx.subscribed_user.email])
