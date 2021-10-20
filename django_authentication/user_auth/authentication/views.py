from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from .forms import CreateUserForm

# user registration using function based view
def register(request):
    form = CreateUserForm(request.POST)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = CreateUserForm()
    
    context = {
        'form' : form
    }
    return render(request,'user/register.html',context)





