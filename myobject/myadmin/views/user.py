import random

from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import User
from datetime import datetime
from django.core.paginator import  Paginator
from django.db.models import Q
import  hashlib
# Create your views here.
def index(request,pIndex=1):
    #try:
        umod = User.objects
        ulist = umod.filter(status__lt=9)
        mywhere = []
        key = request.GET.get("keyword",None)
        if key :
            ulist = ulist.filter(Q(username__contains=key)| Q(nickname__contains=key))
            mywhere.append('keyword='+key)

        pIndex = int(pIndex)
        page = Paginator(ulist,5)
        maxpages = page.num_pages
        if pIndex > maxpages:
            pIndex = maxpages
        if pIndex<1:
            pIndex=1
        list2 = page.page(pIndex)
        plist = page.page_range
        context = {"userslist":list2,'plist':plist,'pIndex':pIndex,'maxpages':maxpages,'total': len(ulist),'mywhere':mywhere}
        return render(request,'myadmin/user/index.html',context)
    #except:
     #   return HttpResponse("user not exits")
def add(request):
    return render(request,'myadmin/user/add.html')
def insert(request):
    try:
        ob = User()
        ob.username = request.POST['username']
        ob.nickname = request.POST['nickname']
        ob.password = request.POST['password']
        ob.status = 1
        ob.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {'info':"Add success!"}

    except Exception as err:
        context = {'info':"Add failed"}
    return render(request,'myadmin/info.html',context)


def delete(request,uid=0):
    try:
        ob = User.objects.get(id=uid)
        ob.status =9
        ob.update_at =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {"info": "delete success"}
    except:
        context = {"info": "delete fail"}
    return render(request, "myadmin/info.html", context)
def edit(request,uid=0):
    try:
        ob = User.objects.get(id=uid)
        context = {"user": ob}
        return render(request, "myadmin/user/edit.html", context)
    except:
        context = {"info": "Can't find user"}
        return render(request, "myadmin/info.html", context)
def update(request,uid=0):
    try:
        ob = User.objects.get(id=uid)
        ob.username = request.POST['username']
        ob.nickname = request.POST['nickname']
        ob.status = request.POST['status']
        ob.password = request.POST['password']
        ob.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        context = {"info": "Edit success"}
    except:
        context = {"info": "Editfail"}
    return render(request, "myadmin/info.html", context)