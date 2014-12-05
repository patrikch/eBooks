from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"home.html")

def list(request):
    return render(request,"list.html")

def search(request):
    return render(request,"advSearch.html")

def keysearch(request):
    return render(request,"keySearch.html")

def detail(request,id):
    return render(request,"detail.html")

    

