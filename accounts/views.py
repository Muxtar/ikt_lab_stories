from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from accounts.forms import RegisterForm


def loginView(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('home'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        print(user, username, password)
        if user:
            login(request, user)
            return redirect(reverse_lazy('home'))
    return render(request, 'login.html')


def logoutView(request):
    logout(request)
    return redirect(reverse_lazy('login'))



def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(request.POST.get('password'))
            user.save()

    context = {
        'forms':form
    }
    return render(request, 'register.html', context)