from django.shortcuts import render
from . import models
from .models import Urls
from django.http import HttpResponseRedirect ,HttpResponse, HttpResponseNotFound
import string , random



def encode(request):
    if request.method == 'POST':
        exist = Urls.objects.filter(long = request.POST.get('long_url_name'))
        if len(exist)<=0:
            strin = '0123456789abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            my_str =''
            for c in range(15):
                my_str += random.choice(strin)
            my_url = Urls(long = request.POST.get('long_url_name') , short = my_str)
            my_url.save()
            return render(request,'home.html',{'short_url_name':my_str})
        else:
            return render(request,'home.html',{'short_url_name':Urls.objects.get(long = request.POST.get('long_url_name'))})

    elif request.method == "GET":
        return render(request,'home.html',{'short_url_name':""})
            



def decode(request, short):
    try:
        link = Urls.objects.get(short=short)
        loong = link.long
        return HttpResponseRedirect(loong)
    except Urls.DoesNotExist:
        return HttpResponseNotFound()
