from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from django.contrib import auth



def menu(request):
    if request.method == 'POST':
        auth.logout(request)
    return render(request, 'menu.html')

