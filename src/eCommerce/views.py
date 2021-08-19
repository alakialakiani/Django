from django.http import HttpResponse
#from django.shortcuts import render


def home_page(request):
	# return HttpResponse("This is Home Page!")
	go_to_about_us = "<a href='/about-us'>Go to about us Page!</a>"
	return HttpResponse(go_to_about_us)


def about_us(request):
	return HttpResponse("This is About us Page!")
