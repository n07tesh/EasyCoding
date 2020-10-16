from django.shortcuts import render,HttpResponse,redirect
from . models import Contact
from . import forms
from django.http import HttpResponseRedirect
# from .forms import MyForm
from django.contrib import messages
from django.views import View
from Blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
#from django.views.generic import(TemplateView)
# Create your views here.
def home(request):
    return render(request,'Home/home.html')
def about(request):
    return render(request,'Home/about.html')


def contact(request):
    if request.method =='POST':
       name = request.POST['name']
       email = request.POST['email']
       phone = request.POST['phone']
       content = request.POST['content']
       print(name,email,phone,content)
       if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
           messages.error(request,"Please fill the form correctly")
       else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,'Your message has been successfully sent')

    return render(request, "Home/contact.html")

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()

    else:

    #allPosts = Post.objects.all()
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
        
    if allPosts.count() == 0:
        messages.warning(request,"No search results found.Please refine your query")
    params = {'allPosts': allPosts,'query':query}
    return render(request,"Home/search.html",params)

   # return HttpResponse('This is seaarch')
   
   #Authenticated APIs
def handleSignup(request):
    if request.method == 'POST':
        #Get the post method parameters
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        #checks for errorneous inputs
        # username should be under 10 characters

        if len(username) > 10:
            messages.error(request,'Username must be under 10 characters')
            return redirect('home')
        # username should be alphanumeric
        if not username.isalnum():
            messages.error(request,'Username should only contain letters and numbers')
            return redirect('home')
        #passwords should match
        if password != password1:
            messages.error(request,'Passwords do not match')
            return redirect('home')
        
        #create the user
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request,"Your EasyCoding account is successfully created")
        return redirect('home')
    else:
        return HttpResponse('404 - Not Found')
   

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Login In")
            return redirect('home')
        
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect('home')
    return HttpResponse('404 - Not Found')

    #return HttpResponse('login')

def handleLogout(request):
    #if request.method == 'POST':
        logout(request)
        messages.success(request,"Successfully Logged Out")
        return redirect('home')
    #else:
        #return HttpResponse('404 - Not Found')

    #return HttpResponse('Logout')
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    #form = forms.Contact(request.POST)

    #if form.is_valid():
        #Do something code
       # print("Validation success!")
       #print("NAME: " + form.cleaned_data['name'])
       #print("PHONE: " + form.cleaned_data['phone'])
       #print('Email: ' + form.cleaned_data['email'])
       #print('Content: ' + form.cleaned_data['content'])
    
    


