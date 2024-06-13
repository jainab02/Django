from django.shortcuts import render
from cbvApp.models import Student

from cbvApp.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404,JsonResponse
# Create your views here.

class StudentList(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)


class StudentDetail(APIView):
    def get_student(self,pk):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        student = self.get_student(pk)
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data,safe=False)
    

    def put(self,request,pk):
        student = self.get_student(pk)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        else:
            return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST,safe=False)
        
    def delete(self,request,pk):
        student = self.get_student(pk)
        student.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT,safe=False)