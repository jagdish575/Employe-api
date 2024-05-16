from django.shortcuts import render
from .models import *
from .serializers import EmployeeSerializer 
from  rest_framework import generics
# Create your views here.


class EmployeeCreateApi(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer



class EmployeeApi(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer


class EmpolyeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer
    

class EmpolyeeDeleteApi(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer
