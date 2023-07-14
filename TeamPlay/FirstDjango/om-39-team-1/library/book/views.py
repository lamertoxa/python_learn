from django.shortcuts import render

def index (request):

    return render(request,'index.html',context={'obj':'book',
        'pic':'https://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/book-icon.png',
        'text':'Here you can find a lot of information about our books'})