from django.shortcuts import render, HttpResponse, reverse, redirect
from bookings.models import UserBooking
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from feedback.models import UserFeedback


def home(request):
	return render(request, 'index.html')

@login_required
def book_now(request):
	return render(request, 'main.html')

def about_us(request):
	if request.method == 'GET':
		ratings = UserFeedback.objects.all()
		return render(request, 'about-us.html', {'ratings':ratings})

def blog(request):
	return render(request, 'blog-single.html')

def contact_us(request):
	return render(request, 'contact.html')

def offers(request):
	return render(request, 'schedule.html')

@cache_control(no_cache=True, must_revalidate=True)
def bookwash(request):
	print(request.POST)
	if request.method == 'POST':
		try:
			if request.POST.get('name') and request.POST.get('email'):
				new_booking = UserBooking()
				
				new_booking.name = request.POST.get('name')
				new_booking.email = request.POST.get('email')
				new_booking.phone = request.POST.get('phone')
				new_booking.address = request.POST.get('addr')
				new_booking.landmark = request.POST.get('landmark')
				new_booking.city = request.POST.get('city')
				new_booking.state = request.POST.get('state')
				new_booking.pincode = request.POST.get('pincode')
				new_booking.booking_date = request.POST.get('date')
				new_booking.prefered_time = request.POST.get('time')
				new_booking.alternate_time = request.POST.get('atime')
				new_booking.car_type = request.POST.get('ctype')
				new_booking.package_type = request.POST.get('package')
				new_booking.addons = request.POST.getlist('addon')
				new_booking.coupon_code = request.POST.get('ccode')
				new_booking.description = request.POST.get('desc')

				new_booking.save()

				return render(request,'redirect.html')
		except Exception:
			return HttpResponseRedirect(reverse('booking_page'))
		
	else:
		return HttpResponseRedirect(reverse('booking_page'))