from django.db import models

class UserFeedback(models.Model):
	IMAGE_DIR_PATH = 'images/'
	IMG_TAG = (
		('exterior', 'exterior'),
		('interior', 'interior'),
		('others', 'others'),
	)

	name = models.CharField(max_length = 30, default = "Ekko User")
	rating = models.IntegerField(default = 4)
	review = models.TextField(default='Quality Service and Friendly Staff, Must try!')
	picture = models.ImageField(upload_to = IMAGE_DIR_PATH)
	picture_tag = models.CharField(max_length = 9, choices = IMG_TAG, default = 'exterior')