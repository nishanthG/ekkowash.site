from django.db import models

class User_Booking(models.Model):
	
	name = models.CharField(max_length = 30)
	email = models.EmailField()
	phone = models.IntegerField()
	address = models.TextField()
	landmark = models.TextField()
	city = models.CharField(max_length=15)
	state = models.CharField(max_length=15)
	pincode = models.IntegerField()
	booking_date = models.DateField()
	prefered_time = models.TimeField()
	alternate_time = models.TimeField()
	car_type = models.TextField()
	addons = models.TextField()
	coupon_code = models.CharField(max_length=10)
	description = models.TextField()
