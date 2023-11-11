from django.shortcuts import render, redirect
from .models import Toot
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def home(request):
    toots = Toot.objects.all()
    return render(request, 'home.html', {'toots': toots})

def toot(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        toot = Toot(user=request.user, content=content)
        toot.save()
        return redirect('home')
    return render(request, 'toot.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

