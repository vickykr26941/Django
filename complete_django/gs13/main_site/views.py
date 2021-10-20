# template inheritance with static files
# overiding templates bloks data

from django.shortcuts import render
def home(request):
    return render(request,'main_site/home.html')

def about(request):
    return render(request,'main_site/about.html')

