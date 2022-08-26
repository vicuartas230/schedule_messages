from django.shortcuts import render
from django.http import HttpResponse
from .forms import MessageForm
from .models.motivational_message import MotivationalMessage

def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            frequency = request.POST['frequency']
            time = request.POST['time']
            title = request.POST['title']
            content = request.POST['content']
            if frequency == 'daily':
                new_message = MotivationalMessage.objects.create(title=title, content=content)
            elif frequency == 'weekly':
                new_message = MotivationalMessage.objects.create(title=title, content=content)
            else:
                new_message = MotivationalMessage.objects.create(title=title, content=content)
            return HttpResponse("Success!...")
    else:
        form = MessageForm()

    return render(request, 'index.html', {'form': form})
