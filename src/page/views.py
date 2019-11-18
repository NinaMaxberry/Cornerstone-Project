import csv

from django.http import HttpResponse # must add to integrate django
from django.shortcuts import render

# Create your views here.
def homepage_view(request, *args, **kwargs):
    my_description = {
        "my_text" : "Description - This site will allow you to see the changes in blah blah blah",
        "my_congTable": "table to show current reps"
    }
    
    return render(request, "home.html", my_description)

def results_view(request, *args, **kwargs):
    my_findings = {
        "my_vision" : "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?",
        "my_table" : "See the table.",
    
    }
    return render(request, 'results.html', my_findings)

def csv_zip_view(request):

    with open(r'zip_code_query.csv') as f:
        reader = csv.reader(f, delimiter=' ', quotechar= '|')
        for column in reader:
            _, created = zip.objects.get_or_create(
                zip=column[0],
                county=column[3]
            )
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