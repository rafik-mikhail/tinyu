from django.urls import path
from . import views

urlpatterns =[
    path('', views.decode, name='decode'), #to long
    path('home', views.encode, name='home'), #to short
]