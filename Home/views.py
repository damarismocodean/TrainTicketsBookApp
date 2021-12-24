from django.template import loader
from Home.models import Person
from .forms import LoginUser, RegisterUser
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def GetHome(request):
    return render(request, 'Homepage.html')


def register_or_login(request):
    template = loader.get_template('RegisterLogin.html')
    if request.method == 'POST':
        if 'login' in request.POST:
            registration_form = RegisterUser()
            login_form = LoginUser(request.POST)
            if login_form.is_valid():
                data = login_form.cleaned_data
                username = data['usernameLog']
                password = data['passwordLog']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('Home/', request)
                return HttpResponse('<h1>Invalid Credentials</h1>')
            return HttpResponse('<h1>Invalid Data Login</h1>')
        elif 'register' in request.POST:
            login_form = LoginUser()
            registration_form = RegisterUser(request.POST)
            if registration_form.is_valid():
                user = registration_form.save(commit=False)
                data = registration_form.cleaned_data
                personA = Person()
                personA.name = data['name']
                personA.username = data['username']
                personA.password = data['password']
                personA.email = data['email']
                personA.number = data['number']
                personA.save()
                user.set_password(personA.password)
                user.save()
                user = authenticate(username=personA.username, password=personA.password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return render(request, 'Homepage.html')
                return HttpResponse('<h1>Invalid Credentials</h1>')
            return HttpResponse('<h1>Invalid Data Registration</h1>')

    return HttpResponse(template.render({}, request))

