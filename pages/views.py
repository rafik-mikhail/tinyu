from django.shortcuts import render
from . import models
from .models import Urls
from django.http import HttpResponseRedirect ,HttpResponse, HttpResponseNotFound
import string , random
def encode(request):
    if request.method == 'POST':
        exist = Urls.objects.filter(long = request.POST.get('name'))
        if len(exist)<=0:
            strin = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345678901234567890123456789'
            my_str =''
            for c in range(15):
                my_str += random.choice(strin)
            my_url = Urls(long = request.POST.get('name') , short = my_str)
            my_url.save()
            return render(request,'home.html',{'name':my_str})
        else:
            return render(request,'home.html',{'name':Urls.objects.get(long = request.POST.get('name'))})

    elif request.method == "GET":
        return render(request,'home.html',{'name':""})
            





def decode(request, short):
    try:
        link = Urls.objects.get(short=short)
        loong = link.long
        return HttpResponseRedirect(loong)
    except Urls.DoesNotExist:
        return HttpResponseNotFound()




# Create your views here.
