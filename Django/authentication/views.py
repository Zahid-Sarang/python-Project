from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"authentication/index.html")


def signup(request):
    return render(request,"authentication/signup.html")

def signin(request):
    return render(request,"authentication/signin.html")


def signout(request):
   pass
