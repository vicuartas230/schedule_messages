from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .forms import MessageForm
from .models.motivational_message import MotivationalMessage
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            frequency = request.POST['frequency']
            time = request.POST['time'].split(':')
            hours = int(time[0])
            minutes = int(time[1])
            title = request.POST['title']
            content = request.POST['content']
            if frequency == 'daily':
                new_message = MotivationalMessage.objects.create(title=title, content=content)
                schedule, created = CrontabSchedule.objects.get_or_create(minute=minutes, hour=hours)
                task = PeriodicTask.objects.create(
                    crontab=schedule,
                    name=new_message.title,
                    task='motivational.tasks.sendEmail',
                    args=json.dumps([new_message.id]),
                    start_time=datetime.now()
                )
            elif frequency == 'weekly':
                new_message = MotivationalMessage.objects.create(title=title, content=content)
                day = datetime.today().weekday()
                schedule, created = CrontabSchedule.objects.get_or_create(
                    minute=minutes,
                    hour=hours,
                    day_of_week=day - 6 if day == 6 else day + 1
                )
                PeriodicTask.objects.create(
                    crontab=schedule,
                    name=new_message.title,
                    task='motivational.tasks.sendEmail',
                    args=json.dumps([new_message.id]),
                    start_time=datetime.now()
                )
            else:
                new_message = MotivationalMessage.objects.create(title=title, content=content)
                day = datetime.now().strftime('%d')
                schedule, created = CrontabSchedule.objects.get_or_create(
                    minute=minutes,
                    hour=hours,
                    day_of_month=day
                )
                PeriodicTask.objects.create(
                    crontab=schedule,
                    name=new_message.title,
                    task='motivational.tasks.sendEmail',
                    args=json.dumps([new_message.id]),
                    start_time=datetime.now()
                )
            return HttpResponse("Success!...")
    else:
        form = MessageForm()

    return render(request, 'index.html', {'form': form})
