from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, localtime, strftime
from django.utils import timezone

def root(request):
    return redirect ("/")


def index(request):
    print(timezone.now())
    context = {
        "date": strftime("%A, %d de %B del %Y", localtime()),
        "time": strftime("%X", localtime()),
    }
    return render(request,'index.html', context)