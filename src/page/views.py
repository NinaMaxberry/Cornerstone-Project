import csv

from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import Http404

from .models import rep

# Create your views here.


def homepage_view(request, *args, **kwargs):
    my_description = {
        "my_text" : "Thanks for your interest in discovering your local congressional district information.  Did you know that your district is determined by your residence zip code?Each zip code points to a county in Kentucky and the counties are grouped into one of six congressional districts.",
        "currentReps" : "The current representatives for all districts are:",
        "letsGo" : "Enter your zip code in the box below",
    }
    
    first_page = rep.objects
    print(first_page)

    return render(request, "home.html", my_description)

def results_view(request, *args, **kwargs):
    my_findings = {
        "my_vision" : "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?",
        "my_table" : "See the table.",
        "dist_outline" : "mapfile",
    }
    return render(request, 'results.html', my_findings)

def index(request):
    letsGo = rep.objects.get(zip)
    #template = loader.get_template('page/index.html')
    #output = ', '.join([i.zip_id for i in letsGo])
    context = {'letsGo' : letsGo}
    #return HttpResponse(template.render(context, request))
    try:
        zip = rep.objects.get(zip)
    except zip.DoesNotExist:
        raise Http404("The zipcode does not exist")
    #return render(request, 'page/noZip.html', {'rep': rep})
    return render(request, 'page/index.html', context)

# def noZip(request, zip):
#     try:
#         zip = rep.objects.get(pk=zip_id)
#     except zip.DoesNotExist:
#         raise Http404("The zip does not exist")
#     return render(request, 'page/noZip.html', {'rep': rep})

    #template = "upload_zip.html"

    #prompt = {
    #    'order': 'Order of the CSV should be zip, county'
    #}

    #if request.method == "GET":  # user lands on page and the template directs them what to do; make sure to include prompt on home page
        #return render(request, template, prompt)

    #csv_file = request.FILES['"C:\Dev\zip_code_database.csv"']  # is ['file'] the actual name of the file?

    #data_set = csv.file.read().decode('UTF-8')
    #io_string = io.StringIO(data_set)   # can I use readline() instead?
    #next(io_string)  # skips the header#

    #for column in csv.reader(io_string, delimiter=',', quotechar="|"):   # quotechar used to remove quotes if file has quotes around data
       # _, created = zip.objects.update_or_create(
           # zip=column[0],
            #county=column[1]
        #)

    context = {}  # future use - to add a message or something specific

    return render(request, context)