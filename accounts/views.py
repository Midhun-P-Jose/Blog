from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator

from . forms import accform
# Create your views here.


@never_cache
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = accform()
    if request.method == 'POST':
        form = accform(request.POST)
        if form.is_valid():
            createduser = form.save()
            login(request,createduser)
            return redirect('signin')
    return render(request,'signup.html',{'form':form})


@never_cache
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username = username,password = password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid username or password')
    return render(request,'signin.html')

@never_cache
def acc_logout(request):
    logout(request)
    return redirect('signin')


    