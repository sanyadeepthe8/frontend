from django.db import models
class StudentModel(models.Model):  
    student_first_name = models.CharField(max_length=30)  
    student_last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10, unique=True)
    roll_no = models.CharField(max_length=8, unique=True)   
    email = models.EmailField()  
  
    def __str__(self):  
        return (self.student_first_name+' '+ self.student_last_name)