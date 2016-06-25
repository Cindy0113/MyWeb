#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import Obj

def home(request):
    rowRange = range(5)
    Objs = Obj.objects.all()
    return render(request, 'home.html',{'obj':Objs})

def index(request):
    return HttpResponse(u"欢迎光临 Cindy的收纳窗！")

