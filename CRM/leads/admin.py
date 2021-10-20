from django.contrib import admin
from leads.models import User,Agent,Lead 

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Lead)
