from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import CustomUser
import logging
from django.contrib.auth.decorators import login_required
@login_required
def main(request):

    return render(request,'home.html')
def  signin(request,user=None):
    if request.method == "GET":
        return render(request,'login.html')
    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
    if user is not None:

        login(request,user)
        return redirect('authentication:main')
    else:
        messages.success(request,("Error, Try Again"))
        return redirect('authentication:signin')

def registration(request):
    if request.method == 'POST':
        data = {key: item for key, item in request.POST.items() if key != 'csrfmiddlewaretoken' and item}
        try:
            user = CustomUser.objects.create_user(**data,is_active=True)
        except:
            user=None
        if user:
            messages.success(request, 'Done')
            return redirect("authentication:signin")
        messages.error(request, "Unsuccessful registration")


    return render(request,'registration.html')

def users(request):
    context = {}
    context["users"]=CustomUser.objects.all()
    return render(request,'users.html',context=context)

def get_user(request,id):

    context = {}
    user = CustomUser.objects.get(id=id)
    context['user'] = user
    return render(request,"user_page.html",context=context)

def exit(request):
    logout(request)
    return redirect('authentication:signin')

