from django.urls import include, path
from django.contrib import admin


from page import views

app_name = 'page'

urlpatterns = [
    path('homepage/', views.homepage_view, name='homepage'),
    path('upload-csv/', views.Csv_upload, name='csv_upload'),
    path('zip/', views.zipUser_view, name = 'zipUsercd'),
    path('results/', views.results_view, name='results_view'),

    
]