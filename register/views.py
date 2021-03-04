from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
        else:
            messages.error(request, 'Username or Email already in use')
            return redirect("/register")
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form":form})


    