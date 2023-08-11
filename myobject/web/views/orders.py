from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from myadmin.models import Category,Product,User
from myadmin.models import Order,OrderDetail,Payment
from datetime import datetime
from django.core.paginator import  Paginator

def index(request,Oindex=1):
    '''view orders'''
    #try:
    omod = Order.objects
    olist = omod.filter(status__lt=6)

    mywhere=[]
    status = request.GET.get("status",'')
    if status !='':
        olist = olist.filter(status=status)
        mywhere.append("status="+status)
    olist = olist.order_by("id")
    pIndex = int(Oindex)
    page = Paginator(olist, 5)
    maxpages = page.num_pages
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)
    plist = page.page_range
    for vo in list2:
        if vo.user_id == 0:
            vo.nickname == "None"
        else:
            user = User.objects.only("nickname").get(id=vo.user_id)
            vo.nickname = user.nickname
    context = {"orderlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, 'total': len(olist),'mywhere':mywhere}
    return render(request, 'web/order/index.html', context)
    #except:
        #return HttpResponse("order does not exits")


def insert(request):
    '''insert order'''
    try:
        od = Order()
        od.user_id = request.session['webuser']['id']
        od.money = request.session['total_money']
        od.status = 1  #1:processing 2: invalid 3:Done
        od.payment_status = 1  #1:unpaid  2:paid 3:refund
        od.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        od.save()

        op = Payment()
        op.order_id = od.id
        op.money = request.session['total_money']
        op.pay_type = request.GET.get("bank",1)   #1:cash 2:card 3:app scan
        op.status = 1 #1:unpaid  2:paid 3:refund
        op.create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.update_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        op.save()

        cartlist = request.session.get("cartlist",{})
        for item in cartlist.values():
            ov = OrderDetail()
            ov.order_id = od.id
            ov.product_id = item['id']
            ov.product_name = item['name']
            ov.price = item['price']
            ov.quantity = item['num']
            ov.status = 1  #1 normal 9:delete
            ov.save()
        del request.session['cartlist']
        del request.session['total_money']

        return HttpResponse("Y")
    except Exception as err:
        print(err)
        return  HttpResponse("N")
def detail(request):
    '''view order detail'''
    oid = request.GET.get("oid",0)
    dlist = OrderDetail.objects.filter(order_id=oid)
    context ={"detaillist":dlist}
    for v in dlist:
        print(v.product_name)
    return render(request,"web/order/detail.html",context)

def status(request):
    '''change orders detail'''
    try:
        oid =request.GET.get("oid",0)
        ob = Order.objects.get(id=oid)
        ob.status = request.GET['status']
        ob.save()
        return  HttpResponse("Y")
    except Exception as err:
        print(err)
        return  HttpResponse("N")

def paymentstatus(request):
    '''change orders detail'''
    try:
        oid =request.GET.get("oid",0)
        ob = Order.objects.get(id=oid)
        ob.payment_status = request.GET['paymentstatus']
        ob.save()
        return  HttpResponse("Y")
    except Exception as err:
        print(err)
        return  HttpResponse("N")




