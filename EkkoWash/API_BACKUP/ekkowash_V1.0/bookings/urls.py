from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_now, name='booking_page'),
    path('about/', views.about_us, name='about_page'),
    path('blog/', views.blog, name='blog_page'),
    path('gallery/', views.gallery, name='gallery_page'),
    path('contact/', views.contact_us, name='contact_us_page'),
    path('offers/', views.offers, name='offers_page'),
    path('book_now/', views.bookwash, name='book_wash')
]