from django import forms
from django.forms import ModelForm
from category.models import Category
from pages.models import Post

class PostModelForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'