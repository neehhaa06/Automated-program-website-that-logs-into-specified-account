from django.shortcuts import render, redirect
from .models import Account
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    accounts = Account.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'accounts': accounts})

@login_required
def add_account(request):
    if request.method == 'POST':
        platform = request.POST['platform']
        username = request.POST['username']
        password = request.POST['password']
        frequency = request.POST['frequency']
        account = Account(user=request.user, platform=platform, username=username, password=password, login_frequency=frequency)
        account.save()
        return redirect('dashboard')
    return render(request, 'add_account.html')
