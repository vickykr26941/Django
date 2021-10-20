from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    class Meta:
        model = User
        fields = ['email','username','password1','password2']

