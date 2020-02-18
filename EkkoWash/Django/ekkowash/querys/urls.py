from django.urls import path
from . import views

urlpatterns = [
	path('', views.contact_us, name='contact_us_page'),
    path('query/', views.send, name='send_query'),
]