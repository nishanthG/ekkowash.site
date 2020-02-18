from django.shortcuts import render, reverse, redirect
from feedback.models import UserFeedback
from django.http import HttpResponseRedirect

def feedback(request):
	return render(request, 'feedback.html')

def user_feedback(request):
	if request.method == "POST":
		
		try:
			feedback = UserFeedback()
			
			if request.POST.get('username') != '':
				feedback.name = request.POST.get('username')
			
			if request.POST.get('star') != '':
				feedback.rating = request.POST.get('star')

			if request.POST.get('feedback') != '':
				feedback.review = request.POST.get('feedback')

			if request.FILES.get('pic') != '':
				feedback.picture = request.FILES.get('pic')

			if request.POST.get('tag') != '':
				feedback.picture_tag = request.POST.get('tag')
			
			feedback.save()
		
		except Exception:
			feedback = UserFeedback()
			return redirect("feedback_page")
	else:
		feedback = UserFeedback()

	return HttpResponseRedirect(reverse('home'))
