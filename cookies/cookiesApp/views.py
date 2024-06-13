from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    request.session.set_test_cookie()
    return HttpResponse("<h2>Home page</h2>")

def page2(request):
    if request.session.set_test_cookie():
        print("Cookies are enabled!")
    request.session.delete_test_cookie()
    return HttpResponse("<b>Page 2</b>")