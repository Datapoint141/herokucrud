from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,"index.html",{'name':'Alex Hales'})
def home(request):
    return render(request,'home.html',{})