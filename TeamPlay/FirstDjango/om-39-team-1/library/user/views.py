from django.shortcuts import render

def index (request):

    return render(request,'index.html',context={'obj':'user',
        'pic':'https://icons.iconarchive.com/icons/icons-land/vista-people/256/Person-Male-Light-icon.png',
        'text':'This is your main page. You can some info about yourself.'})