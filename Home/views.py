from django.template import loader
from Home.models import Person
from .forms import LoginUser,RegisterUser
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def GetHome(request):
    return render(request, 'Home.html')

def LogIn(request):
    template = loader.get_template('Login.html')
    if request.method=='POST':
        form=LoginUser(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            username=data['username']
            password=data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('Home/',request)
            return HttpResponse('<h1>Invalid Credentials</h1>')
        return HttpResponse('<h1>Invalid Data</h1>')
    else:
        return HttpResponse(template.render({}, request))

def Register(request):
    template = loader.get_template('Register.html')
    if request.method=='POST':
        form=RegisterUser(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            data=form.cleaned_data
            nameUser=data['name']
            usernameUser=data['username']
            passwordUser=data['password']
            emailUser=data['email']
            numberUser=data['number']
            personA=Person()
            personA.name = nameUser
            personA.username = usernameUser
            personA.password = passwordUser
            personA.email = emailUser
            personA.number = numberUser
            personA.save()
            user.set_password(passwordUser)
            user.save()
            user=authenticate(username=usernameUser,password=passwordUser)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return render(request, 'Home.html')
            return HttpResponse('<h1>VALID</h1>')
        return HttpResponse(template.render({'form':form},request))
    else:
        return HttpResponse(template.render({},request))
