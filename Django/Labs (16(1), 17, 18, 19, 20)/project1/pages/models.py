from django.db import models
from category.models import Category

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    image = models.CharField(max_length=200,null=True,blank=True)
    version = models.IntegerField(default=1)
    author = models.CharField(max_length=200,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name='posts_category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_image_url(self):
        if self.image:
            return f'/media/{self.image}'
        return ''