from django.urls import path, include
from django.contrib import admin


from . import views

app_name = 'page'
urlpatterns = [
    path('', views.homepage_view, name='homepage_view'),
    path('results/', views.results_view, name='results_view'),
    path('userInput/', views.userInput, name ='User Input'),
    #path('csv_upload/', include('page.urls')), 
    
]