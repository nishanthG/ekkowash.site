from django.db import models

class RegisteredUser(models.Model):

	name = models.CharField(max_length= 30)
	email = models.EmailField()
	password = models.CharField(max_length=20)