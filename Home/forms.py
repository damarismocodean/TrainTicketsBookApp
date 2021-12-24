from django.contrib.auth.models import User
from django import forms

class LoginUser(forms.Form):
    usernameLog = forms.CharField(max_length=100)
    passwordLog = forms.CharField(max_length=20, widget=forms.PasswordInput())

class RegisterUser(forms.ModelForm):
    name = forms.CharField(required=True)
    username=forms.CharField(required=True)
    password = forms.CharField(required=True)
    email = forms.CharField(required=True)
    number=forms.CharField(required=True)

    class Meta:
        model=User
        fields=['name','username','password','email','number']

    def save(self, commit=True):
        user = super(RegisterUser, self).save(commit=False)
        user.name = self.cleaned_data["name"]
        user.username = self.cleaned_data["username"]
        user.password = self.cleaned_data["password"]
        user.email = self.cleaned_data["email"]
        user.number = self.cleaned_data["number"]
        if commit:
            user.save()
        return user