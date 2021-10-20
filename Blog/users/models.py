from django.core import validators
from django.db import models
from django.contrib.auth.models import User

# allow specific file to image field
from django.core.validators import FileExtensionValidator
from django.db.models.fields import Field 

class ProfileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default = 'avtar.jpg',upload_to='profile',validators=[FileExtensionValidator(['png','jpg'])])

    def __str__(self):
        return self.user.username 



