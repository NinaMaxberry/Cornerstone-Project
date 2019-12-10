from django import forms

class EntryForm(forms.Form):
    zipUser = forms.CharField(max_length=5)


    