from django.shortcuts import render, HttpResponse
from gallery.models import Gallery 

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
		return HttpResponse("<h1>Hit !!</h1>")
	# name = request.GET['name']
	# email = request.GET.get('email')
	# phone = request.GET.get('phone')
	# address = request.GET.get('addr')
	# landmark = request.GET.get('landmark')
	# city = request.GET.get('city')
	# state = request.GET.get('state')
	# pincode = request.GET.get('pincode')
	# date = request.GET.get('date')
	# time = request.GET.get('time')
	# atime = request.GET.get('atime')
	# ctype = request.GET.get('ctype')
	# addon = request.GET.get('addon')
	# ccode = request.GET.get('ccode')
	# description = request.GET.get('desc')
