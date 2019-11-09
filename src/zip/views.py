from django.http import HttpResponse # must add to integrate django
from django.shortcuts import render

# Create your views here.
def homepage_view(*args, **kwargs):
    return HttpResponse("<h1>What voting district do you live in?</h1>") #Can use str HTML with django function
