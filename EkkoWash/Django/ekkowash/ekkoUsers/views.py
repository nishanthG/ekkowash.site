from django.shortcuts import render, HttpResponse, reverse, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def login(request):
	if request.method == "POST":
		email = request.POST.get('email')
		password = request.POST.get('password')

		try:
			username = User.objects.get(email = email.lower()).username
			user = auth.authenticate(username = username, password = password)

			if user is not None:
				auth.login(request, user)
				return HttpResponseRedirect(reverse('home'))
			
			else:
				messages.error(request, 'Invalid credentials.')
				return redirect('login_page')

		except Exception:
			messages.error(request, 'Invalid credentials.')
			return redirect('login_page')	
	else:
		return render(request, 'login_page.html')


def signup(request):
	return render(request, 'signup_page.html')

def logout(request):
	auth.logout(request)
	return redirect('home')

def register(request):
	if request.method == "POST":
		try:
			username = request.POST.get('username')
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			
			if request.POST.get('password') == request.POST.get('conf_password'):
				password = request.POST.get('password')

				if not User.objects.filter(username = username).exists() and not User.objects.filter(email = email).exists():
					
					new_user = User.objects.create_user(username = first_name +' '+ last_name,
						password = password, email = email, first_name = first_name, last_name = last_name)

					new_user.save();
				else:
					messages.info(request,'email already registered.')	
					return redirect('signup_page')	
			
			else:
				messages.info(request,'Passwords do not match')
				return redirect('signup_page')
		
		except Exception:
			return redirect('signup_page')

	return HttpResponseRedirect(reverse('login_page'))