from django import forms

class EntryForm(forms.Form):
    zip_by_user = forms.IntegerField(help_text='Use 5 digits only')
    