from django.shortcuts import render
from . import models
from .models import Urls
from django.http import HttpResponseRedirect
def encode(request):
    return HttpResponseRedirect('http://www.google.com')





def decode(request):
    link = Urls.objects.filter(short=request.path)
    loong = link.long
    return HttpResponseRedirect(loong)





# Create your views here.
