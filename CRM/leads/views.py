from django.shortcuts import redirect, render,reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lead,Agent
from .forms import LeadForm, LeadModelForm,CustomeUserCreationForm
from django.views.generic import (
    TemplateView, ListView, CreateView,DeleteView,UpdateView,DetailView
)

# auth permission(allow relvelt resources to revelent people)

# django autontication (implemented builtin autontication provide by django)
# LoginView, LogoutView taken from builtin django , created custome Signup view with inheriting CreateView 

# LoginRequiredMixin is same as login_required decorator in functional
class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomeUserCreationForm

    def get_success_url(self) -> str:
        return reverse('login')

# CRUD -> Create, Retrive, Update and Delte and List 



# we can create views using class based views and function based views
# class based views 
# in class based views we need to write very less code 
# there is some generic view like, CreateView, DeleteView, UpdateView we can inherit these genric builtin view and can do more stuff 
# that make django easy and less code 


# function based views 
def landing_page(request):
    return render(request, 'landing.html')


# this class based view is same as above function based view 
class LandingPageView(TemplateView):
    template_name = "landing.html"


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads" : leads,
    }
    return render(request, 'leads/lead_list.html',context)

# above list view using class 
class LeadListView(LoginRequiredMixin,ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all()
    # data will be passed automatically as object_list to the template by default , we can change that too see below code 
    context_object_name = 'leads'



def lead_detail(request,pk):
    lead = Lead.objects.get(id = pk)
    context = {
        'lead' : lead,
    }
    return render(request,"leads/lead_detail.html",context)

# above lead detail view as using class view method 
class LeadDetailView(LoginRequiredMixin,DetailView):
    template_name = 'leads/lead_detail.html'

     # we need not to specify the primay key here it will automatically detect
    # queryset = Lead.objects.all()
    context_object_name = 'lead'

    # we can get_queryset as we want to filter 
    def get_queryset(self,*args,**kwargs):
        return Lead.objects.filter(id=self.kwargs['pk'])


  # creating form using normal mehtod 
  # we can create the django form with already existing model in easiery way 

# def lead_create(request):
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent
#             )
#             return redirect('/leads')
#         else:
#             print('first enter the valid input to the form')
    
#     context = {
#         'form' : form
#     }
#     return render(request,"leads/lead_create.html",context)



# form created using Django Model form
def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid() : 
            form.save()
            return redirect('/leads')
        else:
            print('enter the data properly')
    context = {
        'form' : form 
    }
    return render(request,'leads/lead_create.html',context)

# lead create view using class 
class LeadCreateVeiw(LoginRequiredMixin,CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm 

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')



# lead update form // normal 

# def lead_update(request,pk):
#     lead = Lead.objects.get(id = pk)
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST,instance=lead)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             lead.first_name = first_name
#             last_name = last_name 
#             lead.age = age 
#             lead.save()
#         return redirect('/leads')
#     else :
#         form = LeadModelForm(instance=lead)
    
#     context = {
#         'form' : form,
#         'lead' : lead
#     }
#     return render(request,'leads/lead_update.html',context)


# creating update form uisng djagno model form 

def lead_update(request,pk):
    form = LeadModelForm()
    lead = Lead.objects.get(id = pk)
    if request.method == 'POST':
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid() : 
            form.save()
            return redirect('/leads')
    else:
        form = LeadModelForm(instance=lead)
    context = {
        'form' : form,
        'lead' : lead 
    }
    return render(request,'leads/lead_update.html',context)

class LeadUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'leads/lead_update.html'
    queryset = Lead.objects.all()
    form_class = LeadModelForm 

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')
 


def lead_delete(request,pk):
    lead = Lead.objects.get(id = pk)
    lead.delete()
    return redirect('/leads')

# delte viw using class 

class LeadDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse("leads:lead-list")


    