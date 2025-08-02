from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from pages.models import Post
from category.models import Category

# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request, 'category/index.html',context={'categories':categories})

def details(request,id):
    category =Category.objects.get(id=id)
    return render(request, 'category/details.html',context={'category':category})

def update_category(request,id):
    category = get_object_or_404(Category,id=id)
    if request.method == 'GET':
        form = PostModelForm(instance=category)
        return render(request, 'category/editform.html',context={'form':form})
    elif request.method == 'POST':
        form = PostModelForm(request.POST,request.FILES,instance=category)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('category.index')
        return redirect('category.index')

def delete_category(request,id):
    category = get_object_or_404(Category,id=id)
    category.delete()
    return redirect('index')

def create_category(request):
    if request.method == 'GET':
        form = PostModelForm()
        return render(request, 'category/createform.html',context={'form':form})
    elif request.method == 'POST':
        form = PostModelForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('category.index')
        return redirect('category.index')