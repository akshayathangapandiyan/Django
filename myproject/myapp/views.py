from django.shortcuts import render
from django.http import HttpResponse
#from.models import employee
from.models import jaishaa
from models import student_signals
#from.models import student
#from myapp.models import employee
from.models import student_ser
from rest_framework import viewsets
from.serializers import StudentSerializer

# Create your views here.
def home(request):
    return HttpResponse('Welcome To django...')

#employee.objects.create(name ="akshuu")

#student.objects.create(name = "atchuuu",age = 20,mark = 89,subject = "computer application")

# jaishaa.objects.create(name = "jay", age =20,mark = 89,sub = "computer apllication")



class StudentViewSet(viewsets.ModelViewSet):
    queryset = student_ser.objects.all()
    serializer_class = StudentSerializer


student_signals.objects.create(name = "akshu", age = 20)