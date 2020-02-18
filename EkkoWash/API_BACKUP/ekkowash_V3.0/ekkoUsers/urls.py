from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login_page'),
    path('signup/', views.signup, name='signup_page'),
    path('register/', views.register, name='register_user'),
]