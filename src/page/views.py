from django.http import HttpResponse # must add to integrate django
from django.shortcuts import render

# Create your views here.
def homepage_view(request, *args, **kwargs):
    #return HttpResponse("<h1>What voting district do you live in?</h1>") #Can use str HTML with django function
    return render(request, "home.html", {})

def constanttext_view(request, *arg, **kwargs):
    return HttpResponse("<h2>How have the districts changed?</h2>")
