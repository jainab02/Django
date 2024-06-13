from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def display(request):
    return HttpResponse("<h1>Hey there!</h1>")


def displayTime(request):
    t = datetime.datetime.now()
    d = datetime.date.today()
    time = "<b>current date and time is </b>"+str(t) +"<br>" "Date is " + str(d)
    return HttpResponse(time)