from django.shortcuts import render
from gallery.models import Gallery
from feedback.models import UserFeedback

def user_upload_images(request):
	if request.method == 'GET':
		gallery = UserFeedback.objects.all()
		return render(request, 'gallery.html', {'gallery':gallery})