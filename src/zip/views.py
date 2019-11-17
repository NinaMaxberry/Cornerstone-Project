from django.shortcuts import render
from .models import Zip

# Create your views here.
def zip_code_view(request):

    return render(request, "zip_code/detail.html", {})