from django.urls import include, path
from django.contrib import admin


#from page.views import homepage_view, csvUpload, zipUser_view, results_view

from page import views

app_name = 'page'

urlpatterns = [
    
    path('home/', views.homepage_view, name='homepage_view'),
    path('upload/', views.csvUpload, name='csv_upload'),
    path('zip/', views.zipUser_view, name = 'zipUser_view'),
    path('results/', views.results_view, name='results_view'),
    path('ky_outline/', views.display_ky_image, name = 'ky_image'),
    
]