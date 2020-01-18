from django import forms
from .models import *

# class EntryForm(forms.Form):
#     zipUser = forms.CharField(label="Enter your zipcode"  max_length=5)
       
#     def acceptable(self):
#         accept_data = super(EntryForm, self).clean()
#         zipUser = accept_data.get("zipUser")
#         p = KentuckyProject.objects.all()
#         if zipUser:
#             for i in p:
#                 if i.zip not in zipUser:
#                     raise forms.ValidationError(
#                         "Zipcode does not exist")

# class EntryForm(forms.Form):
#     zipUser = forms.CharField(label="Enter your zipcode", max_length=5)

    
# class KyForm(forms.ModelForm):

#     class Meta:
#         model=KyImage
#         fields = ['name', 'outlineImg']  

# class homeIntro(forms.Form):
#     my_text = forms.CharField(max_length=500)

    
    
    #return render (request, 'userInput.html', my_selection)


    # try:
    #     findZip=input("Enter your zipcode: ")
    #     for x in district.objects.get(zip):
    #         findZip == zip
    # except zip.DoesNotExist:
    #     raise Http404()
    #     return HttpResponse(district.objects(congressional_district))
    # else:
    #     findZip != zip
    #     raise Http404("The zipcode does not exist. Please try again.")

    #     findName = district.objects(congressional_district)
    # for x in district.objects.get(f_name, l_name):

    #     return render(request, context)   

