from django.db import models
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import AbstractUser 
   # django builtin user model
# User = get_user_model()  -> this give us default user model of django 



# creating our custome user mode
class User(AbstractUser):
    def __str__(self) -> str:
        return self.username 
        
# Leads -> customers 
class Lead(models.Model):
    # SOURCE_CHOICES = {
    #     ('YouTube','YouTube'),
    #     ('Google','Google'),
    #     ('Newsletter','Newsletter'),

    # }
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent",on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    # some important Fields that might be used in some cases
    # like choice filed, imagefile,filefield etc 


    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES,max_length=100)
    # progile_picture = models.ImageField(blank = True, null = True)

    # special_files = models.FileField(blank=True, null=True) 
    



# Agent -> Agent can manage lots of leads so Agent should be the parent table for the leads 
class Agent(models.Model):
       # every Agent is a user 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.user.email


# admin-> vicky
# email-> vickykr26941@gmail.com 
# pass -> vickykr123@