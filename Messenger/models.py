from django.db import models


# Create your models here.
class User(models.Model):
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	contact=models.CharField(max_length=100)
	logged_in=models.BooleanField(default=False)
	def __str__(self):
		return self.username

class Message(models.Model):
	receiver=models.ForeignKey(User)
	sender=models.CharField(max_length=100,default="shivam")
	message_text=models.TextField(default="your message")
	def __str__(self):
		return self.message_text

	