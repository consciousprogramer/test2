from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello! world")

def newview(request):
    return HttpResponse("newview added")

def branchview(request):
    return HttpResponse("this is branch view")
