from django.shortcuts import render
from django.template import loader
def displaygreen(request):
    stu=[{'name':'Sanya','marks':90},{'name':'Deepthe','marks':85},
         {'name':'Priya','marks':88},{'name':'Pooja','marks':91}]

    return render(request,'green.html',{'data': stu})
## def displaygreen(request):
##    stu=['shiva','navmohan','shravani','salma']
##    return render(request,'green.html',{'data': stu})