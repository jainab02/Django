from django.shortcuts import redirect, render

from fbvApp.models import Student
from fbvApp.forms import StudentForm

# Create your views here.
def getStudent(request):
    students= Student.objects.all()
    return render(request, 'fbvApp/index.html', {'students':students})
    # return render(request,'fbvApp/index.html',students)

def createStudent(request):
    form = StudentForm()
    if request.method =='POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'fbvApp/create.html',{"form": form})

