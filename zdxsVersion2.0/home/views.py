#-*- coding: UTF-8 -*- 

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from blog.models import Blog
from data.models import Data

from .forms import RegisterForm,LoginForm

# Create your views here.

def index(request):
    return render(request,'home_index.html')
    
def register(request):
    
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=User.objects.create_user(
                username=form.cleaned_data['name'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                )
            user.save()    
            return HttpResponseRedirect('/login')
    else:
        form=RegisterForm()
    
    return render(request,'home_register.html',{'form':form})
    
def login(request):
    errors=[]
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            try:
                username=User.objects.get(email=form.cleaned_data['email']).username
            except User.DoesNotExist:
                errors.append('这个邮箱没有用户')
            else:
                user=authenticate(username=username,password=form.cleaned_data['password'])
                if user is not None:
                    if user.is_active:
                        auth_login(request,user)
                        return HttpResponseRedirect('/')
                    else:
                        errors.append('你的用户没有激活')
                else:
                    errors.append('错误的用户名或密码')
            
                
    else:
        form=LoginForm()
    return render(request,'home_login.html',{'form':form,'errors':errors})
     
def person(request,name):
    try:
        the_user=User.objects.get(username=name)
    except User.DoesNotExist:
        raise Http404
    try:
        blogs=Blog.objects.filter(editor__exact=name)
    except Blog.DoesNotExist:
        blogs=[]
    try:
        datas=Data.objects.filter(editor__exact=name)
    except Data.DoesNotExist:
        datas=[]
    return render(request,"home_person.html",{"the_user":the_user,"datas":datas,"blogs":blogs})


                    
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')            
        

def my_404_view(request):
    return render(request,'my_404.html')