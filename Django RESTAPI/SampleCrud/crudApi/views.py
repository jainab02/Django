# from io import BytesIO
import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from crudApi.models import Student
from crudApi.serializers import StudentSerializer
# Create your views here.

def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondta = JSONParser().parse(stream)
        id = pythondta.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type = 'application/json')
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many = True)
        json_data= JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type = 'application/json')




