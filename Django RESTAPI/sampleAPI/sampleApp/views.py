from django.shortcuts import render
from rest_framework import viewsets
from sampleApp.models import *
from sampleApp.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class SampleViewSets(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

    @action(detail=True,methods = ['GET'])
    def employees(self,request,pk = None):
        # print("This is sample "+pk)
        company = Sample.objects.get(pk=pk)
        # print(company)
        emps = Employee.objects.filter(company_name= company)
        empSerializer = EmpSerializer(emps,many = True)
        print(empSerializer)
        return Response(empSerializer.data)
        

class EmpViewSets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmpSerializer
    
