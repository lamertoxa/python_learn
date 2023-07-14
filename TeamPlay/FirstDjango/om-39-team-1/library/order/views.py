from django.shortcuts import render

def index (request):

    return render(request,'index.html',context={'obj':'order',
        'pic':'https://icons.iconarchive.com/icons/custom-icon-design/flatastic-5/512/Order-history-icon.png',
        'text':'This is page for creating and submitting your orders'})