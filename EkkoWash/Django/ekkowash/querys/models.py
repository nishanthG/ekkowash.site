from django.db import models

class ContactQuery(models.Model):

	name = models.CharField(max_length = 30)
	email = models.EmailField()
	phone = models.IntegerField()
	message = models.TextField()