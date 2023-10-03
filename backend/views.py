from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def home(req:HttpRequest):
    if req.method == "GET":
        print("hello")
    elif req.method == "POST":
        ...
    return render(req, "login.html", {})