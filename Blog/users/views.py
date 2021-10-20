from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from users.models import ProfileModel
from .forms import CustomeUserCreationForm,ProfileUpdateForm, UserUpdateForm 

def signup(request):
    if request.method == 'POST':
        form = CustomeUserCreationForm(request.POST)
        if form.is_valid() : 
            form.save()
            return redirect('user-login')
    else:
        form = CustomeUserCreationForm()
    context = {
        'form' : form
    }
    return render(request,'users/sign_up.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST or None ,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST or None, request.FILES or None,instance=request.user.profilemodel)
        if user_form.is_valid() and profile_form.is_valid() : 
            user_form.save()
            profile_form.save()
            return redirect('user-profile')

    else:
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(request.FILES,instance=request.user.profilemodel)

    context = {
        'user_form': user_form,
        'profile_form' : profile_form
    }
    return render(request,'users/profile.html',context)
    