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

# class homepage_view(TemplateView):
#     template_name = 'home.html'
#     correct_url = '/thanks/'

#     def get(self, request):
#         form = EntryForm
#         return render()


def homepage_view(request):
    my_description = {
        "my_text" : "Thanks for your interest in discovering your past and present local congressional district information.  Did you know that your district is determined by your residence zip code?  Each zip code points to a county in Kentucky and the counties are grouped into one of six congressional districts.  We will look at the representatives from the 110th Congress (year 2000) with your zip code and compare them with your present representatives (116th Congress).",
        "home_title" : "How The Congressional Districts In KY Have Changed Through The Census",

    }
    return render(request, 'home.html', my_description)
    
    # def form_valid(self, form):
    #     return super().form_valid(form)

    
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

    #def acceptable(self):
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


def display_ky_image(request):
    template = 'display_ky_image.html'
    if request.method == 'GET':

        KyImages = KyImage.objects.all()
    return render(request, template)


    



# def KyImage_view(request):
#     if request.method == 'POST':
#         form = KyForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = KyForm()
#     return render (request, 'kyimage.html', {'form' : form})

# def success(request):
#     return HttpResponse('successfully uploaded')


    
    
    
    
    
    
    
    
    
    
    
    #useZip=input("Enter your zipcode: ")
    #template = loader.get_template('page/userInput.html')
    #context = {'userInput': ''}
    
    # try:
    #     usezip = zip.objects.get(zip)
    #     return HttpResponse(template.render(context, request)) #double check - should it be content=b''

    # except usezip.DoesNotExist:
    #         raise Http404("The zipcode does not exist. Please try again.")

    # return render(request, 'page/userInput.html', context, {'userInput': userInput})

    
    

    


    
    