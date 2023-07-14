from django.shortcuts import render

def index (request):

    return render(request,'index.html',context={'obj':'main page',
        'pic':'https://icons.iconarchive.com/icons/google/noto-emoji-objects/1024/62868-page-facing-up-icon.png',
        'text':'Welcome at our library web-cite! We are glad to see you here!'})