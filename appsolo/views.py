from django.shortcuts import render
from django.http import HttpResponse
from .models import viktorina,internet,mobile_internet,television
def index(requst):
    new = viktorina.objects.all()

    return render(requst,'appsolo/index.html',{'new': new})

def inet(requst):
    new1 = internet.objects.all()

    return render(requst,'appsolo/internet_diz.html',{'new1': new1})

def mobile_inet(requst):
    new2 = mobile_internet.objects.all()

    return render(requst,'appsolo/mobile_inet.html',{'new2': new2})

def telev(requst):
    new3 = television.objects.all()

    return render(requst,'appsolo/television.html',{'new3': new3})