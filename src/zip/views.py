import csv

from django.shortcuts import render
from .models import Zip

# Create your views here.
def csv_zip_view(request):

    with open(r'zip_code_query.csv') as f:
        reader = csv.reader(f, delimiter=' ', quotechar= '|')
        for column in reader:
            _, created = zip.objects.get_or_create(
                zip=column[0],
                county=column[3]
            )
