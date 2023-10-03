from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def auth_home(req: HttpRequest)-> HttpResponse:
    return HttpResponse("hello world")


def auth_login(req: HttpRequest):
    return render(req, "login_.html")

def auth_signup(req: HttpRequest):

    return render(req, "signup.html")