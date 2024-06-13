from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    mydata={"name":"Zainab"}
    return render(request,'templatesApp/firstTemplate.html',context=mydata)

def renderEmployee(request):
    mydata1 ={"id":1,"name":"zainab","role":"intern","salary":100000}
    return render(request,'templatesApp/employeeTemp.html',context=mydata1)