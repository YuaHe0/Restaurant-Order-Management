import random

from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import User
from myadmin.models import Category
from datetime import datetime
from django.core.paginator import  Paginator

import  hashlib
# Create your views here.
def index(request,pIndex=1):
    try:
        umod = Category.objects
        ulist = umod.filter(status__lt=6)
        mywhere = []
        key = request.GET.get("keyword", None)
        if key:
            ulist = ulist.filter(name__contains=key)
            mywhere.append('keyword=' + key)

        pIndex = int(pIndex)
        page = Paginator(ulist,5)
        maxpages = page.num_pages
        if pIndex > maxpages:
            pIndex = maxpages
        if pIndex<1:
            pIndex=1
        list2 = page.page(pIndex)
        plist = page.page_range
        context = {"categorylist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'total': len(ulist),'mywhere':mywhere}
        return render(request,'myadmin/category/index.html',context)
    except:
        return HttpResponse("Category not exits")
def add(request):
    return render(request,'myadmin/category/add.html')


def insert(request):
    try:
        ob = Category()
        ob.name = request.POST['name']
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"Add success!"}

    except Exception as err:
        context = {'info':"Add failed"}
    return render(request,'myadmin/info.html',context)


def delete(request,cid=0):
    try:
        ob = Category.objects.get(id=cid)
        ob.status =9
        ob.update_at =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {"info": "Delete success"}
    except:
        context = {"info": "Delete fail"}
    return render(request, "myadmin/info.html", context)
def edit(request,cid=0):
    try:
        ob = Category.objects.get(id=cid)
        context = {"category": ob}
        return render(request, "myadmin/category/edit.html", context)
    except:
        context = {"info": "Can't find category"}
        return render(request, "myadmin/info.html", context)
def update(request,cid=0):
    try:
        ob = Category.objects.get(id=cid)
        ob.name = request.POST['name']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {"info": "Edit success"}
    except:
        context = {"info": "Editfail"}
    return render(request, "myadmin/info.html", context)