from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def  mca(request):
    temp=loader.get_template('mca.html')
    return HttpResponse(temp.render())