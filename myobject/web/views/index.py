from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse

from myadmin.models import Category
from myadmin.models import Product
from myadmin.models import User
import  hashlib
# Create your views here.
def index(request):
    return  redirect(reverse("web_index"))

def webindex(request):

    pmod = Product.objects
    plist = pmod.filter(status__lt=6)

    cmod = Category.objects
    clist = cmod.filter(status__lt=6)
    cartlist = request.session.get('cartlist', {})
    total_money = 0
    for vo in cartlist.values():
        total_money += int(vo['num'])*float(vo['price'])

    request.session['total_money'] = total_money
   # print(request.session.get("categorylist",{}).items())
    context = {"productlist":plist,"categorylist":clist}

    return render(request,'web/index/index.html',context)
def login(request):
    return  render(request,'web/index/login.html')

def dologin(request):
    try:
        user = User.objects.get(username=request.POST['username'])
        print(user.username)
        if user.status == 6:
            #md5 = hashlib.md5()
            #s = request.POST['password']+user.password_salt
            #md5.update(s.encode('utf-8'))
            #if user.password_hash == md5.hexdigest():
            if user.password == request.POST['password']:
                request.session['webuser']=user.toDict()
                clist = Category.objects.filter(status__lt=6)
                categorylist = dict()
                productlist = dict()
                for vo in clist:
                    c = {'id': vo.id, 'name': vo.name, 'pids': []}
                    plist = Product.objects.filter(category_id=vo.id)
                    for p in plist:
                        c['pids'].append(p.toDict())
                        productlist[p.id] = p.toDict()
                        categorylist[vo.id] = c
                request.session['categorylist'] = categorylist
                request.session['productlist'] = productlist

                return redirect(reverse("web_index"))
            else:
               context = {'info':'password incorrect'}


        else:
            context = {'info':'Account does not have permission'}


    except Exception as err:
        print(err)
        context = {'info':'account dose not exist'}
    return render(request,'web/index/login.html',context)
def logout(request):
    del request.session['webuser']
    return redirect(reverse('web_login'))
def type(request,Cid):
    pmod = Product.objects
    plist = pmod.filter(status__lt=6)
    plist2 = plist.filter(category_id=Cid)

    cmod = Category.objects
    clist = cmod.filter(status__lt=6)

    context = {"productlist": plist2,"categorylist":clist}
    return render(request, 'web/index/index.html',context)