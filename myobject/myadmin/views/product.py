import random

from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import User
from myadmin.models import Category
from myadmin.models import Product
import time,os
from datetime import datetime
from django.core.paginator import  Paginator


import  hashlib
# Create your views here.
def index(request,pIndex=1):
    try:
        umod = Product.objects
        ulist = umod.filter(status__lt=6)
        mywhere = []
        key = request.GET.get("keyword", None)
        if key:
            ulist = ulist.filter(name__contains=key)
            mywhere.append('keyword=' + key)

        cid = request.GET.get("category_id", None)
        if cid:
            ulist = ulist.filter(category_id=cid)
            mywhere.append('category_id=' + cid)

        pIndex = int(pIndex)
        page = Paginator(ulist,5)
        maxpages = page.num_pages
        if pIndex > maxpages:
            pIndex = maxpages
        if pIndex<1:
            pIndex=1
        list2 = page.page(pIndex)
        plist = page.page_range
        for vo in list2:
            cob = Category.objects.get(id=vo.category_id)
            vo.categoryname = cob.name

        context = {"productlist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'total': len(ulist),'mywhere':mywhere}
        return render(request,'myadmin/product/index.html',context)
    except:
        return HttpResponse("Product not exits")
def add(request):
    clist = Category.objects.values("id","name")
    context={"categorylist":clist}
    return render(request,'myadmin/product/add.html',context)


def insert(request):
    #try:
        myfile = request.FILES.get('pic')
        print(myfile)
        #if not myfile:
         #   return  HttpResponse("no picture")
        cover_pic = str(time.time())+"."+myfile.name.split('.').pop()
        destination = open("./static/uploads/product/"+cover_pic,"wb+")
        for chunk in myfile.chunks():
            destination.write(chunk)
        destination.close()

        ob = Product()
        ob.category_id = request.POST['category_id']
        ob.name = request.POST['name']
        ob.print = request.POST['price']
        ob.cover_pic = cover_pic
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"Add success!"}

   # except Exception as err:
      #  context = {'info':"add failed"}
        return render(request,'myadmin/info.html',context)


def delete(request,pid=0):
    try:
        ob =Product.objects.get(id=pid)
        ob.status =9
        ob.update_at =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {"info": "Delete success"}
    except:
        context = {"info": "Delete fail"}
    return render(request, "myadmin/info.html", context)
def edit(request,pid=0):
    try:
        ob =Product.objects.get(id=pid)
        clist = Category.objects.values("id", "name")
        context = {"categorylist": clist,"product": ob}
        return render(request, "myadmin/product/edit.html", context)
    except:
        context = {"info": "Can't find product"}
        return render(request, "myadmin/info.html", context)
def update(request,pid=0):
    try:
        ob = Product.objects.get(id=pid)
        ob.name = request.POST['name']
        ob.status = request.POST['status']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {"info": "Edit success"}
    except:
        context = {"info": "Edit fail"}
    return render(request, "myadmin/info.html", context)