from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from books import forms
from books import models
from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage
from django.contrib.auth import logout

ITEMS_PER_PAGE = 5

def home(request):
    return render(request,"home.html")

def list(request):
    sortExpr = None
    if "sort" in request.GET:
        sortParam = request.GET["sort"]
        print("sort:" + sortParam)
        sortParam = sortParam.replace("Plus","+")
        sortParam = sortParam.replace("Minus","-")
        sortExpr = models.BookRep().sort(sortParam)
        print("sortExpr:" + sortExpr)
        
    if sortExpr == None:
        allbooks = models.Book.objects.all()
    else:
        allbooks = models.Book.objects.all().order_by(sortExpr)
    
    paginator = Paginator(allbooks,ITEMS_PER_PAGE)
    try:
        page_number = int(request.GET["page"])
    except (KeyError, ValueError):
        page_number = 1
    try:
        page = paginator.page(page_number)
    except InvalidPage:
        raise Http404

    books = page.object_list
    dict = {
        "books":books,
        "show_paginator": paginator.num_pages > 1,
        "has_prev": page.has_previous(),
        "has_next": page.has_next(),
        "page": page_number,
        "pages": paginator.num_pages,
        "next_page": page_number + 1,
        "prev_page": page_number - 1
        }
    return render(request,"list.html",dict)

def search(request):
    books = []
    if request.method == "POST":        
        print("POST")
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            #print("spojka:" + form.cleaned_data["spojka"] + "\n")
            #print("name:" + form.cleaned_data["name"] + "\n")
            #print("authors:" + form.cleaned_data["authors"] + "\n")
            #print("publisher:" + form.cleaned_data["publisher"] + "\n")
            #print("location:" + form.cleaned_data["location"] + "\n")
            #print("pubYear:" + str(form.cleaned_data["pubYear"]) + "\n")
            #sort = request.POST["txtsort"]
            sort = form.cleaned_data["sort"]
            print("sort:" + sort)
            #for key in request.POST:
            #    value = request.POST[key]
            #    print(key + ":" + value)
                
            bookRep = models.BookRep()
            books = bookRep.find(form.cleaned_data["spojka"],form.cleaned_data["name"],form.cleaned_data["authors"],
                             form.cleaned_data["publisher"],form.cleaned_data["location"],
                             form.cleaned_data["pubYear"],sort)            
    else:        
        #print("GET")
        form = forms.SearchForm()
        
    return render(request,"advSearch.html",{"form":form,"books":books})    

def keysearch(request):
    return render(request,"keySearch.html")

def detail(request,id):
    return render(request,"detail.html")

def logout(request):
    logout(request)
    return HttpResponseRedirect("/")
    



    

