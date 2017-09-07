from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

from .models import Blog
def blogbs(request):
    context = {
        "title" : "Nazhier Rijalana"
    }
    return render(request,"index.html",context)
def myblog(request):
    context = {
        "title" : "Blog Nazhier Rijalana"
    }
    return render(request, "myblog.html", context)
def account(request):
    if request.user.is_authenticated():
        context = {
            "title" : "Admin/staff Profile"
        }
        return render(request,'myblog.html',context)
    else:
        return render(request,'200.html')
