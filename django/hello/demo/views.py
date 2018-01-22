from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime

def index(request):
    response = "<b>Hello</b> from index ... "
    return HttpResponse(response)

def showtime(r):
    t = datetime.now()
    r ="current time: " + t.strftime("%A, %d. %B %Y %I:%M:%S")
    return HttpResponse(r)

def testError1(request): # my page not found
    return HttpResponseNotFound('<h1>Page not found</h1>')    

def testError2(request): # response status
    return HttpResponse(status=400)



