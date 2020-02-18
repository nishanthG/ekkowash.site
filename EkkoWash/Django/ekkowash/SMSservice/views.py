from django.shortcuts import render
from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def sms_response(request):
	resp = MessagingResponse()

	msg = resp.message("Check out this sweet owl!")
	msg.media("https://demo.twilio.com/owl.png")

	return HttpResponse(str(resp))