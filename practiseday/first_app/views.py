from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,update_session_auth_hash,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home (request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            messages.success(request,'Accaunt Created Successfuly')
            register_form.save()
            return redirect('login')
    else:
        register_form = forms.RegisterForm()
    return render(request,'register.html',{'form':register_form,'type':'Register'})

def user_login(request):
    if request.method == 'POST':
        form =AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = user_name,password = user_pass)
            if user is not None:
                messages.success(request,'Logged in Successfuly')
                login(request,user)
                return redirect('profile')
            else:
                messages.success(request,'Login in Information incorrect')
                return redirect('profile')
    else:
        form =AuthenticationForm()
    return render(request,'register.html',{'form':form,'type':'Login'})

@login_required
def pass_change1(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password update Successfully')
            update_session_auth_hash(request,request.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'pass_change.html',{'form':form})

@login_required
def pass_change2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user,data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password update Successfully')
            update_session_auth_hash(request,request.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request,'pass_change.html',{'form':form})

@login_required
def profile(request):
    return render(request,'profile.html')

def user_logout(request):
    messages.success(request,'Logged Out Successfully')
    logout(request)
    return redirect('login')