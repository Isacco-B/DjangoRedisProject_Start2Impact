from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponseRedirect
from .forms import RegisterForm

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            User.objects.create_user(
                username=username,
                password=password,
                email=email,
            )
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = RegisterForm()
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

