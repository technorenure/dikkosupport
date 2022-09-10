from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Registeration, LocalGovt, GroupType


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RegisterationForm(forms.ModelForm):
    class Meta:
        model = Registeration
        fields = '__all__'
