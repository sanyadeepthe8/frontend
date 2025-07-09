from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def  engineering(request):
    temp=loader.get_template('engineering.html')
    return HttpResponse(temp.render())