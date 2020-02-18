from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_upload_images, name='gallery_page'),
]