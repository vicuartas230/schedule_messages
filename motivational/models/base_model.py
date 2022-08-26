from django.db import models


class BaseModel(models.Model):
	is_active = models.BooleanField(default=True)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True
		
	def __str__(self):
		return str(self.pk)
