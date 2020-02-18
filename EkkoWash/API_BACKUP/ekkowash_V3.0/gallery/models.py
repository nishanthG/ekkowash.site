from django.db import models

class Gallery():
	username : str
	user_review : str
	image : str
	image_type : str

	def __init__(self, username, user_review, image, image_type):
		self.username = username
		self.user_review = user_review	
		self.image = image
		self.image_type = image_type
