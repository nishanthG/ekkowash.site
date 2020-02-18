from django.shortcuts import render, HttpResponse, reverse, redirect
from ekkoUsers.models import RegisteredUser
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password

def login(request):
	return render(request, 'login_page.html')

def signup(request):
	return render(request, 'signup_page.html')

def register(request):
	if request.method == "POST":
		try:
			user = RegisteredUser()
			user.name = request.POST.get('username')
			user.email = request.POST.get('email')
			
			if request.POST.get('password') == request.POST.get('conf_password'): 
				user.password = make_password(request.POST.get('password'))

				user.save()
			else:
				return redirect("signup_page")
		
		except Exception:
			return redirect("signup_page")
	else:
		form = RegisteredUser()

	return HttpResponseRedirect(reverse('login_page'))