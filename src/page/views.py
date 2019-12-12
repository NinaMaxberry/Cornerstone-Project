from django.urls import path
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views.generic import TemplateView, FormView

from . import models

from page.forms import forms

# Create your views here.

class homepage_view(TemplateView):
    template_name = 'home.html'
    correct_url = '/thanks/'

    def get(self, request):
        form = EntryForm
        return render()


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
        "my_vision" : "During the 110th Congress, the following were the congressional representatives for Kenutcky.",
        "my_return" : "Your Kentucky Congressional District is:", #need to connect to zipcode search thru database for results - execute on html? Double check db for 2000 data
        "dist_outline" : "mapfile", # should be in static files as image - transparent
    }

    return render(request, 'results.html', my_findings)


def zipUser_view(request):

    if request.method == "GET":
        form = EntryForm()

    if form.is_valid():
        zipUser_view = EntryForm.cleaned_data['zipUser_view']

        # zipUser_view = EntryForm()

    return render(request, 'home.html', {'form': form})


# def EntryForm(self, get):
#         my_selection = {
#             zip_form : forms.EntryForm()
#     }

    # return render (request, 'userInput.html', my_selection)


#     try:
#         findZip=input("Enter your zipcode: ")
#         for x in district.objects.get(zip):
#             findZip == zip
#     except zip.DoesNotExist:
#         raise Http404()
        # return HttpResponse(district.objects(congressional_district))
    # else:
        # findZip != zip
        # raise Http404("The zipcode does not exist. Please try again.")

    #     findName = district.objects(congressional_district)
    # for x in district.objects.get(f_name, l_name):

        # return render(request, context)
# def repList_view(request):
#     all_objects=Rep.objects.all()
#     currRepList = {'all_objects': all_objects}

#     return render (request, 'base.html', currRepList)

# def zips(response):  #to match zips with input and db
#     zipper = ProjectCode.objects.get(zip=zip)
#     return HttpRespnse("<h1>%s</h>")




    
    
    
    
    
    
    
    
    
    
    
    #useZip=input("Enter your zipcode: ")
    #template = loader.get_template('page/userInput.html')
    #context = {'userInput': ''}
    
    # try:
    #     usezip = zip.objects.get(zip)
    #     return HttpResponse(template.render(context, request)) #double check - should it be content=b''

    # except usezip.DoesNotExist:
    #         raise Http404("The zipcode does not exist. Please try again.")

    # return render(request, 'page/userInput.html', context, {'userInput': userInput})

    
    

    


    
    