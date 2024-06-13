from django.shortcuts import render

# Create your views here.
def pageCount(request):
    count = request.session.get('count',0)
    count = count+1
    request.session['count']= count
    return render(request,'sessionApp/count.html',{'count':count})