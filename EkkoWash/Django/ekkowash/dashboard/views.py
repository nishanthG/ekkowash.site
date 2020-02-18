from django.shortcuts import render, reverse, redirect
from feedback.models import UserFeedback
from django.http import HttpResponseRedirect


def dashboard(request):
	return render(request, 'dashboard.html')

def charts(request):
	return render(request, 'chart.html')

def table(request):
	return render(request, 'table.html')

def calendar(request):
	return render(request, 'calendar.html')