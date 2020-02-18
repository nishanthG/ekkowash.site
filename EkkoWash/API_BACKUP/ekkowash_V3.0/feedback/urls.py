from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback, name='feedback_page'),
    path('submit/', views.user_feedback, name='user_feedback'),
]