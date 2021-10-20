
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields 
from .models import ProfileModel 


class CustomeUserCreationForm(UserCreationForm) : 
    email = forms.EmailField()
    class Meta:
        model = User 
        fields = ['email','username','password1','password2']

    def __init__(self, *args, **kwargs) -> None:
        super(CustomeUserCreationForm,self).__init__(*args, **kwargs)
        
        for fieldname in ['email','username','password1','password2'] : 
            self.fields[fieldname].help_text = None 


class UserUpdateForm(forms.ModelForm):
    class Meta : 
        model = User 
        fields = ['username','email']
    
    def __init__(self,*args,**kwargs):
        super(UserUpdateForm,self).__init__(*args,**kwargs)
        for fieldname in ['username','email']:
            self.fields[fieldname].help_text = None 

class ProfileUpdateForm(forms.ModelForm):
    class Meta : 
        model = ProfileModel 
        fields = ['image']
        