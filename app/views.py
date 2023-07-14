from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def Home(request):

    data= Student.objects.all()
    
    return render(request,"app/home.html",{'data':data})

def Student_add(request):
    if request.method == "POST":
       Name = request.POST.get('Name')
       roll_number = request.POST.get('Roll_Number')
       email = request.POST.get('Email_address')
       Class = request.POST.get('Class')

       Stu = Student(name=Name, roll_number=roll_number, email=email, Class=Class)
    
       Stu.save()
           
    
    return render(request,"app/std_add.html")

def Student_delete(request,id):

    data= Student.objects.get(id=id)
    data.delete()
    return redirect("home")

# def Student_updates(request,id):

#     data= Student.objects.all(id=id)
#     if data.is_valid():
#         data.save()
#         return redirect("home")
    
#     return render(request,"app/update.html",{'data':data})

def Student_updates(request,id):

    data= Student.objects.get(id=id)
    
    return render(request,"app/update.html",{'data':data})

def Student_updatesSave(request,id):
    
       Name = request.POST.get('Name')
       roll_number = request.POST.get('Roll_Number')
       email = request.POST.get('Email_address')
       Class = request.POST.get('Class')

       data = Student.objects.get(id=id)
       data.name = Name
       data.roll_number=roll_number
       data.email=email
       data.Class=Class
       data.save()
       return redirect("home")
    
    