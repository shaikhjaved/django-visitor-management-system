from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.


def onGetLogin(request):
    return render(request, 'login.html')


def onPostLogin(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if not username:
            messages.error(request, 'username canot be empty')
            return redirect('accounts:login')
        elif not password:
            messages.info(request, 'password canot be empty')
            return redirect('accounts:login')
        else:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home:index')
            else:
                messages.info(request, 'invalid login credentials')
                return redirect('accounts:login')
    else:
        return render(request, 'login.html')


def onPostLogout(request):
    auth.logout(request)
    return redirect('accounts:login')
