from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def  mba(request):
    temp=loader.get_template('mba.html')
    return HttpResponse(temp.render())