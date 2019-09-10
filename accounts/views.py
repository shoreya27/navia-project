from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method=="POST":
        user=auth.authenticate(request,username=request.POST['email'],password=request.POST['password'])
        if user is None:
            return  render(request,'login.html',{'error':'invalid credentials!!'})
        else:
            auth.login(request,user)
            return redirect('detail')
    return render(request,'login.html')


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')

def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['email'])
                return  render(request,'signup.html',{'error':'user email already exist'})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['email'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return  render(request,'signup.html',{'error':'password do not match!!'})

    else:
        return render(request,'signup.html')
