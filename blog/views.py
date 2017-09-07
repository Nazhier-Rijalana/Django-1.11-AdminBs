from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .Form import BlogForm
from .models import *

# Create your views here.

from .models import Blog
'''
def bloghome(request):
    return render(request,"index.html",{})
    #return HttpResponse("<body background='/home/teiyasa/Pictures/photo1.PNG'><div> <h1><center>Hello World this is my first site</center></h1> <p>tukang ketik males ya gini ngetik view doang aja males apalagi cari jodoh dasar jomblo :v </p></div></body><div> <p><center>Powered By Django 1.9</center></p>")
def blogtest(request):
    testqueryset = Blog.objects.all()
    context = {
        "title": "Blog ketiga",
        "testqset": testqueryset
    }
    return render(request, "blogtest.html", context)
    #return HttpResponse("<body background='/home/teiyasa/Pictures/photo1.PNG'><div> <h1><center>Hello World this is my first site</center></h1> <p>tukang ketik males ya gini ngetik view doang aja males apalagi cari jodoh dasar jomblo :v </p></div></body><div> <p><center>Powered By Django 1.9</center></p>")
def blog88(request):
    if request.user.is_authenticated():
        context = {
            "title": "Second Blog"
        }
        asem = render(request, "index2.html", context)
        return asem
    else:
        context = {
            "title": "yeee mau ngehek ya :v"
        }
        return render(request,"200.html", context)
    #return HttpResponse("<body background='/home/teiyasa/Pictures/photo1.PNG'><div> <h1><center>Hello World this is my secondblog</center></h1> <p>tukang ketik males ya gini ngetik view doang aja males apalagi cari jodoh dasar jomblo :v </p></div></body><div> <p><center>Powered By Django 1.9</center></p>")
def detail(request, id=None):
    instance = get_object_or_404(Blog, id=id)
    context = {
        "title" : "test Detail kan :v ",
        "instance" : instance
    }
    return render(request,"Detail.html", context)

    #return HttpResponse("<body background='/home/teiyasa/Pictures/photo1.PNG'><div> <h1><center>Hello World this is my first site</center></h1> <p>tukang ketik males ya gini ngetik view doang aja males apalagi cari jodoh dasar jomblo :v </p></div></body><div> <p><center>Powered By Django 1.9</center></p>")
def blog44form(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
         instance = form.save(commit=False)
         print form.cleaned_data.get("title")
         instance.save()
    # if request.method=="POST":
    #     print request.POST.get("content")
    #     print request.POST.get("title")
    context = {
        "form" : form,
        "title" : "Post Kata kata"
    }
    return render(request,"BlogForm.html",context)
'''
def blogbs(request):
    context = {
        "title" : "Login"
    }
    return render(request,"index.html",context)