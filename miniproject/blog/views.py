from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from blog.forms import signupforms,loginforms,Postform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import upload

# Create your views here.
def Home(request):
    posts=upload.objects.all()
    return render(request,'blog/home.html',{"pst":posts})

# def user_login(request):
#     if request.method=='POST':
#         fm=AuthenticationForm(request=request,data=request.POST)
        
#Abouy Page
def about(request):
    return render(request,'blog/about.html')
def contact(request):
    return render(request,'blog/contact.html')
def dashboard(request):
    if request.user.is_authenticated:
     posts=upload.objects.all()
     return render(request,'blog/dashboard.html',{'pst':posts})
    else:
       return HttpResponseRedirect('/login/')
def user_login(request):
    if not request.user.is_authenticated:

      if request.method=="POST":
        form=loginforms(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Login success fully')
                return HttpResponseRedirect('/dashboard/')
      else:        
        form =loginforms()
      return render(request,'blog/login.html',{'form':form})
    else:
      return HttpResponseRedirect('/dashboard/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
def user_signup(request):
    if request.method=="POST":
        form=signupforms(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation ')
            form.save()
    else:
        form =signupforms()
    return render(request,'blog/signup.html',{'form':form})
def add_post(request):
   if request.user.is_authenticated:
      if request.method=="POST":
         form=Postform(request.POST)
         if form.is_valid():
            title=form.cleaned_data['title']
            desc=form.cleaned_data['desc']
            pst=upload(title=title,desc=desc)
            pst.save()
            form=Postform()
      else:
         form=Postform()  
      return render(request,'blog/add.html',{'form':form})   
   else:
      return HttpResponseRedirect('/login/')
      
      
             
  # if request.user.is_authenticated:
  #     if request.method == 'POST':
  #       form=Postform(request.POST)
  #       if form.is_valid():
  #          title=form.cleaned_data['title']
  #          desc=form.cleaned_data['desc']
  #          pst=upload(title=title,desc=desc)
  #          pst.save()
  #       else:
  #          form=Postform()
  #     else:
  #       form=Postform()
       
  #     return render(request,'blog/add.html',{'form':form})
  # else:
  #     return HttpResponseRedirect('/login/')
  


def update_post(request,id):
  if request.user.is_authenticated:
     return render(request,'blog/updatepost.html')
  else:
      return HttpResponseRedirect('/login/')
def delete_post(request,id):
  if request.user.is_authenticated:
     return HttpResponseRedirect('/dashboard/')
  else:
      return HttpResponseRedirect('/login/')
   
   