from django.shortcuts import redirect
from django.urls import reverse
import re


class Middleware:
    def __init__(self,get_response):
        self.get_response = get_response


    def __call__(self, request):
        response = self.get_response(request)

        path = request.path
        urllist = ['/myadmin/login','/myadmin/logout','/myadmin/dologin']
        if re.match(r'^/myadmin',path) and (path not in urllist):
           if 'adminuser' not in request.session:
                return redirect(reverse("myadmin_login"))


        #if sign in for web
        if re.match(r'^/web',path):
            if 'webuser' not in request.session:
                return redirect(reverse("web_login"))

        return response