from django.shortcuts import render
from django.http import HttpResponse
from books import forms
from books import models
from django.db.models import Q

def home(request):
    return render(request,"home.html")

def list(request):
    return render(request,"list.html")

def search(request):
    print("in search")
    if request.method == "POST":        
        print("POST")
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            print("spojka:" + form.cleaned_data["spojka"] + "\n")
            print("name:" + form.cleaned_data["name"] + "\n")
            print("authors:" + form.cleaned_data["authors"] + "\n")
            print("publisher:" + form.cleaned_data["publisher"] + "\n")
            print("location:" + form.cleaned_data["location"] + "\n")
            print("pubYear:" + str(form.cleaned_data["pubYear"]) + "\n")
            models.BookRep().find(form.cleaned_data["spojka"],form.cleaned_data["name"],form.cleaned_data["authors"],
                             form.cleaned_data["publisher"],form.cleaned_data["location"],
                             form.cleaned_data["pubYear"])
    else:        
        print("GET")
        form = forms.SearchForm()
        
    return render(request,"advSearch.html",{"form":form})    

def keysearch(request):
    return render(request,"keySearch.html")

def detail(request,id):
    return render(request,"detail.html")



    

