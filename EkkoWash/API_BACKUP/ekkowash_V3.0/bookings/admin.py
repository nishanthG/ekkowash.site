from django.contrib import admin
from bookings.models import UserBooking

admin.site.register(UserBooking)

admin.site.site_url = "http://localhost:8000/ekko/app/"