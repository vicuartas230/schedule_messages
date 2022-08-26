from django.db import models
from .base_model import BaseModel
from datetime import datetime

class MotivationalMessage(BaseModel):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = models.CharField(max_length=500)
