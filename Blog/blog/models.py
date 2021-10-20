from django.db import models
from django.contrib.auth.models import User 

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    class Meta : 
        ordering = ('-date_created',)
    
    def comment_count(self):
        return self.comment_set.all().count()
    
    def __str__(self) : 
        return f'{self.title}' 


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.content 

    