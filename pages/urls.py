from django.urls import path
from . import views

urlpatterns =[
    path('<str:short>', views.decode, name='decode'), #to long
    path('', views.encode, name='home'), #to short
]