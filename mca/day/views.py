from django.shortcuts import render
from .models import StudentModel  
from .forms import StudentForm

from django.http import HttpResponse
from django.template import loader
#display & save form data   
def insert_student(request):
    context ={}# dictionary for initial data with field names as keys
    ob_form = StudentForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_student.html", context)
def operations(request):
    temp=loader.get_template('operations.html')
    return HttpResponse(temp.render())
