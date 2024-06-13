from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/')
def ExpensePage(request):
    budget = 0
    if request.method =='POST':
        data = request.POST
        budget = int(data.get('budget',0))
        name = data.get('name')
        price = int(data.get('price',0))
        Finance.objects.create(
            name=name,
            price=price,
            budget=budget
        )
        return redirect('/home')
    queryset= Finance.objects.all()
    totalExp = sum(finance.price for finance in queryset)
    # print(totalExp)
    context = {'expenses': queryset, 'totalExp': totalExp}
    return render(request,'finance/homePage.html',context=context)

def deleteExp(request,id):
    queryset = Finance.objects.get(id=id)
    queryset.delete()
    return redirect('/home')

def updateExp(request,id):
    queryset = Finance.objects.get(id=id)
    if request.method=='POST':
        data = request.POST
        name = data.get('name')
        price =int(data.get('price',queryset.price))
        queryset.name = name
        queryset.price = price
        queryset.save()
        return redirect('/home')
    context = {"finance":queryset}
    # print(context)
    return render(request,'finance/updateExp.html',context=context)

def registerPage(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = User.objects.filter(username=username)
        user = User.objects.filter(username=username)
        print(user.exists())
        if not user.exists:
            messages.error(request,"Username already exists")
            return redirect('/register')
        
        user = User.objects.create(
            username = username,
            password=password
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Registered successfully!')
        return redirect('/')
    return render(request,'finance/register.html')

def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Username doesnot exists!')
            return redirect('/')
        user = authenticate(username=username,password=password)
        if user :
            login(request,user)
            return redirect('/home')
        else:
            messages.error(request,'Invalid Password')
            return redirect('/')
    return render(request,'finance/login.html')

def logoutPage(request):
    messages.info(request,'Logout Successfully!')
    logout(request)
    return redirect('/')
