from django import forms
from datetime import datetime

FREQUENCIES = [
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly')
]

class MessageForm(forms.Form):
    frequency = forms.CharField(label='Frequency', widget=forms.Select(choices=FREQUENCIES))
    time = forms.TimeField(label='Time')
    title = forms.CharField(label='Title', max_length=100)
    content = forms.CharField(label='Content', max_length=5000, widget=forms.Textarea())
