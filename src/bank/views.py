from django.shortcuts import render, redirect
from .models import Account
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    print(f"{request.user} logged in")
    return render(request, 'bank/index.html')