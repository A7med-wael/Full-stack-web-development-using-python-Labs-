
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from pages.models import Post
from category.models import Category

# Create your views here.
def base(request):
    return render(request, 'base.html')

def products(request):
    return render(request, 'products.html')

def contactus(request):
    return render(request, 'contactus.html')

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html',context={'posts':posts})

def details(request,id):
    post = Post.objects.get(id=id)
    return render(request, 'details.html',context={'post':post})

def delete_post(request,id):
    post = get_object_or_404(Post,id=id)
    post.delete()
    return redirect('index')

def create_post(request):
    if request.method == 'GET':
        form = PostModelForm()
        return render(request, 'createform.html',context={'form':form})
    elif request.method == 'POST':
        form = PostModelForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('index')
        return redirect('index')
    
def update_post(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method == 'GET':
        form = PostModelForm(instance=post)
        return render(request, 'editform.html',context={'form':form})
    elif request.method == 'POST':
        form = PostModelForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('index')
        return redirect('index')