from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard_page'),
    path('analytics/', views.charts, name='chart_page'),
    path('users/', views.table, name='table_page'),
    path('calendar/', views.calendar, name='calender_page'),
]