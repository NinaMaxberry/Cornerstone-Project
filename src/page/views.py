from django.http import HttpResponse # must add to integrate django
from django.shortcuts import render

# Create your views here.
def homepage_view(request, *args, **kwargs):
    my_description = {
        "my_text" : "Description - This site will allow you to see the changes in blah blah blah",
        "my_congTable" : "Your Senator is your Rep is",
        "my_zipList" : [40934, 40237, 46378]
    }
    
    return render(request, "home.html", my_description)

def results_view(request, *args, **kwargs):
    my_findings = {
        "my_vision" : "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?",
        "my_table" : "See the table.",
    
    }
    return render(request, "results.html", my_findings)