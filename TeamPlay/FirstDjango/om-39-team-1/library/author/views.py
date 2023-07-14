from django.shortcuts import render

def index (request):

    return render(request,'index.html',context={'obj':'author',
        'pic':'https://icons.iconarchive.com/icons/icons-land/vista-people/256/Occupations-Writer-Male-Light-icon.png',
        'text':'Here you can find some information about authors of our books'})
