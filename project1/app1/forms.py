from django import forms
from .models import userdata

class LoginForm(forms.ModelForm):
    class Meta:
        model=userdata
        fields=('Email','Password')

class SignupForm(forms.ModelForm):
    class Meta:
        model=userdata
        fields=('Name','Age','Place','Phone','Email','Password')

class UpdateForm(forms.ModelForm):
    class Meta:
        model=userdata
        fields=('Name','Age','Place','Phone','Email')

class ChangePassword(forms.ModelForm):
    class Meta:
        model=userdata
        fields=('OldPassword','NewPassword','ConfirmPassword')