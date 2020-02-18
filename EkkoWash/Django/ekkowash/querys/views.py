from querys.models import ContactQuery
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, reverse, redirect

def contact_us(request):
	return render(request, 'contact.html')

def send(request):
	if request.method == "POST":
			try:
				query = ContactQuery()
				
				query.name = request.POST.get('username')
				query.email = request.POST.get('email')
				query.message = request.POST.get('msg')
				query.phone = request.POST.get('phone')
				
				query.save()
			
			except Exception:
				query = ContactQuery()
				return redirect("contact_us_page")
	else:
		query = ContactQuery()
		return redirect("home")

	return HttpResponseRedirect(reverse('home'))