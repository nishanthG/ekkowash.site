from django.shortcuts import render, HttpResponse, reverse
from gallery.models import Gallery
from bookings.models import User_Booking
from django.http import HttpResponseRedirect
from django.contrib import messages

def home(request):
	return render(request, 'index.html')

def book_now(request):
	return render(request, 'main.html')

def about_us(request):
	return render(request, 'about-us.html')

def blog(request):
	return render(request, 'blog-single.html')

def contact_us(request):
	return render(request, 'contact.html')

def gallery(request):
	gallery1 = Gallery("Nishanth","Awesome Service and Friendly staff.", 'gallery/gallery-1.jpg', "exterior")
	gallery2 = Gallery("George","Good Service and Eco Friendly.", 'gallery/gallery-2.jpg', "others")
	gallery3 = Gallery("Naveen","Fast Service and time saving.", 'gallery/gallery-3.jpg', "interior")
	gallery4 = Gallery("Namratha","Must go for.", 'gallery/gallery-4.jpg', "others")
	gallery5 = Gallery("Kolli","Saved my time and Friendly staff.", 'gallery/gallery-8.jpg', "exterior")
	gallery6 = Gallery("Kshama","Would recommend Everyone to go for it.", 'gallery/gallery-6.jpg', "interior")
	gallery7 = Gallery("Nitesh","Thumbs up.", 'gallery/gallery-7.jpg', "exterior")
	gallery8 = Gallery("Nishanth","Awesome Service and Friendly staff.", 'gallery/gallery-6.jpg', "others")
	gallery9 = Gallery("George","Saved my time and Friendly staff.", 'gallery/gallery-9.jpg', "interior")

	gallery = [gallery1,gallery2,gallery3,gallery4,gallery5,gallery6,gallery7,gallery8,gallery9]

	return render(request, 'gallery.html', {'gallery':gallery})

def offers(request):
	return render(request, 'schedule.html')

def bookwash(request):
	if request.method == 'POST':
		try:
			if request.POST.get('name') and request.POST.get('email'):
				new_booking = User_Booking()
				
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
				new_booking.addons = request.POST.get('addon')
				new_booking.coupon_code = request.POST.get('ccode')
				new_booking.description = request.POST.get('desc')

				new_booking.save()

				return render(request, 'redirect.html')
		except Exception:
			return HttpResponseRedirect(reverse('booking_page'))
		
		else:
			return HttpResponseRedirect(reverse('booking_page'))
