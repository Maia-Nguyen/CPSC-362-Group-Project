from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def logout(request):
    auth.logout(request)
    return redirect('home_url')
