import io, csv

from django.urls import path
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.generic import TemplateView, FormView


from . import models

from page.forms import *

# Create your views here.


def homepage_view(request):
    my_description = {

        "home_title" : "How The Congressional Districts In KY Have Changed Through The Census",

        "my_text1" : "Every ten years, the US Census Bureau conducts a survey to measure changes (+/-) in several areas of the economy across the country. These areas include concentrations or shifts in population, employment, income, poverty and many other areas.",

        "my_text2" : "One of the areas that are affected by the census is your voting rights or more formally stated how voting district boundaries are drawn using the census. Did you know that your district is determined by your residence zip code in Kentucky?  Each zip code points to a county in Kentucky and the counties are grouped into one of six congressional districts. (Note: some zip codes cross county lines).",

        "my_text3" : "Congress holds two sessions during one year, but for simplicity, we will only present the specific Census years.",

        "my_text4" : "We will look at the representatives from the 106th Congress (Census year 2000), the representatives from the  111th Congress (Census year 2010) and compare them with your zip code of your present representatives (116th Congress) of today.",

        "start" : "Below you will find options to search for the representative in your district for 2000, 2010 and now. Will the same representive exist for all years or will there be different representatives based on the zip code you enter?",
    }
    
    return render(request, 'home.html', my_description)


def results_view(request):
    my_findings = {
        "my_vision" : "During the 110th Congress (year 2000), the following were the congressional representatives for Kenutcky.",
        "my_return" : "Your Kentucky Congressional District is:", #need to connect to zipcode search thru database for results - execute on html? Double check db for 2000 data
        "dist_outline" : "mapfile", # should be in static files as image - transparent
    }

    return render(request, 'results.html', my_findings)


def zipUser_view(request):

    if request.method == "POST":
        form = EntryForm(request.POST)

    def acceptable(self):
        if form.is_valid():
            try:
                p = KentuckyProject.objects.get(zip)  #to match zip

                accept_data = (EntryForm, self).clean()
                zipUser = accept_data.get("zipUser")

                #zipUser = EntryForm.cleaned_data['zipUser']

            except KentuckyProject.DoesNotExist:
                raise forms.ValidationError("The zipcode does not exist")
            
        return redirect('results/')

   





        # zipUser_view = EntryForm()

    #return render(request, 'results.html', {'form': form})





def csvUpload(request):
    template = "csv_upload.html"
    
    prompt = {
        'order': 'Order of the CSV should be Zip, District, CongressDistrict, First_Name, Last_Name, message',
           
    }

# GET request for all data
    if request.method == "GET":
        return render (request, template, prompt)

    csv_file = request.FILES['file']

#Is csv file a valid csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)  #create stream of input or output validation to loop through the data
    next(io_string)  #next row is read - header skipped

    for column in csv.reader(io_string, delimiter= ', ', quotechar="|"):
        _, created = Csv.objects.update_or_create(
#identify index/order of each column
            zip = column[0],
            primary_city = column[1],
            county = column[2],
            area_codes = column[3],
            message = column[4]

        )
    context = {}
    return render(request, template, context )





    





    
    
    
    
    
    
    
    
    
    
    
    
    
    

    


    
    