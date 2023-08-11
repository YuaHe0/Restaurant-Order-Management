from django.shortcuts import render
from django.http import HttpResponse
from myadmin.models import User
import  hashlib
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,'myadmin/index/index.html')

def login(request):
    return  render(request,'myadmin/index/login.html')

def dologin(requset):
    print("good2")
    try:
        user = User.objects.get(username=requset.POST['username'])
        print(user.username)
        print(user.password)
        print(requset.POST['password'])
        if user.status == 6:
            #md5 = hashlib.md5()
            #s = requset.POST['password']+user.password_salt
            #md5.update(s.encode('utf-8'))
            #print(md5.hexdigest())
            #if user.password_hash == md5.hexdigest():
            if user.password == requset.POST['password']:
                requset.session['adminuser']=user.toDict()
                return redirect(reverse("myadmin_index"))
            else:
               context = {'info':'Password incorrect'}
        else:
            context = {'info':'Account does not have permission'}

    except Exception as err:
        print(err)
        context = {'info':'Account dose not exist'}
    return render(requset,'myadmin/index/login.html',context)



def logout(request):
    del request.session['adminuser']
    return redirect(reverse('myadmin_login'))