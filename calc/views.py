from fnmatch import fnmatchcase
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method ==  "POST":
        username= request.POST.get("user")
        password = request.POST.get("passw")

        user=auth.authenticate(username=username,password=password)

        if user is not None:
           return render(request, "home.html")

        else:
            return HttpResponse("invalid credentials")
    else:

        return render(request,'Signin.html')

def signup(request):

    if request.method ==  "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        phoneno = request.POST.get("phoneno")
        dob = request.POST.get("dob")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email=request.POST.get("email")
        rques = request.POST.get("rques")
        rans = request.POST.get("rans")

        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = name
        myuser.last_name = surname
    

        myuser.save()

        messages.success(request, "Your account succesfully created")

        return redirect('home')


    return render(request, "signup.html")

def signout(request):
    pass

def main(request):
    return render(request, "home.html")
