from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login as user_login,authenticate


import re

def split_error_message(error_message):
    error_text = re.findall(r'<li>(.*?)</li>', error_message)
    return error_text

# REGISTER METHOD
def Register(request):
    
    if request.user.is_authenticated:
        return redirect("HomePage")
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        
        if form.is_valid():
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request,f"email already exists!")
                return redirect("Register")

            form.save()
            messages.success(request,f"Account Created has been created!You are now able to Login")
            return redirect("Login")
        else:
            error_message=str(form.errors)
            error_text=split_error_message(error_message)
            
            for error in error_text:
                error=error.split("<ul class=\"errorlist\"><li>")
                messages.error(request,f"{error[0]} : {error[1] } ")

    else:
        form=UserRegisterForm()    
    context={
        'title':'Register',
        'form':form,
    }
    return render(request,'Users/Register.html',context)



def login(request):
    
    if request.user.is_authenticated:
        return redirect("HomePage")

    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.filter(email=email).first()
        if user is None:
            messages.error(request,f"User not exist.!")
            return redirect("Login")
        user = authenticate(request, email=email, password=password)
        # user=authenticate(username=user.username,password=password)
        if user is not None:
            if user.is_active:
                user_login(request,user)
                messages.success(request,f"You LogIn successfully.!")
                return redirect("HomePage")
            else:
                messages.error(request,f"disabled account")
        
        else:
            messages.error(request,f"Email or password incorrect.!")

    context={
        'title':'login',
    }

    return render(request,'Users/Login.html',context)

# ACCOUNT METHOD
@login_required
def Profile(request):
    context={
        'title':'Account',
    }
    return render(request,'Users/User.html',context)


#LOGOUT 
def Logout(request):
    logout(request)
    messages.success(request,f"User Logout Successfully!")
    return redirect("Login")