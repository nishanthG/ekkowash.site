"""ekkowash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ekkowash import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('home', permanent=False)),
    path('admin/', admin.site.urls),
    path('ekko/app/', include('bookings.urls')),
    path('ekko/app/user/', include('ekkoUsers.urls')),
    path('ekko/app/feedback/', include('feedback.urls')),
    path('ekko/app/gallery/', include('gallery.urls')),
    path('ekko/app/contact/', include('querys.urls')),
    path('ekko/app/admin/dashboard/', include('dashboard.urls')),
    path('ekko/app/sms/', include('SMSservice.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)