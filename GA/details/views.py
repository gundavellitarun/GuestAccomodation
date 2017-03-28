from django.shortcuts import render
from .models import *

# Create your views here.
def details(request):
    return render(request,'guestdetails/details.html',{})


#function for storing data from HTML into Data base
def add_details(request):
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        indate=request.POST['indate']
        outdate=request.POST['outdate']
        age = request.POST['age']
        relation = request.POST['relation']
        purpose = request.POST['purpose']
        hostels = request.POST['hostels']
        t1 = detail.objects.create(name=name,Gender=gender,age=age,Indate=indate,Outdate=outdate,relation=relation,purpose=purpose,hostelsavailable=hostels)
        return render(request, 'guestdetails/home.html', {})




def intro(request):
    return render(request,'guestdetails/home.html')

def homepage(request):
    data=detail.objects.all()

    stu={
        "data":data
    }


    return render(request,'guestdetails/homepage.html',stu)

