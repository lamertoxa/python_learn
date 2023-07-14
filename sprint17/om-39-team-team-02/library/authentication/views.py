import logging
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from . import models

from django.core.exceptions import PermissionDenied

from .forms import SignInForm,RegistrationForm
from django.contrib import messages



def reg_func_librarian(request):
    if request.method == 'POST':
        email = request.POST['email']
        pas1 = request.POST['password1']
        pas2 = request.POST['password2']
        ac_pas = request.POST['access_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        middle_name = request.POST['middle_name']
        if ac_pas != "qwerty":
            raise PermissionDenied
        if pas1 == pas2:
            user = models.CustomUser.objects.create_librarian(email=email, password=pas1)
            models.CustomUser.update(user, first_name=first_name, last_name=last_name, middle_name=middle_name)
            if user.email:
                return redirect('/auth')
    return render(request, 'reg_librarian.html')

def reg_func_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()
            login(request,user)
            messages.success(request, 'You have successfully registered')
            return redirect('/auth')

        messages.error(request, "Invalid entered data.")
    form = RegistrationForm
    return render(request, 'reg_user.html',{'form':form})

def log_func(request):

    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            logging.warning(f"{email,password}")
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")


    form = SignInForm()
    return render(request, 'log.html',{'reg_form':form})
