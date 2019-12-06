from django.urls import path, include
from django.contrib import admin


from . import views

app_name = 'page'
urlpatterns = [
    path('', views.homepage_view, name='homepage_view'),
    path('Rep/', views.repList, name='rep_list'),
    path('userInput/', views.userInput, name ='User Input'),
    path('results/', views.results_view, name='results_view'),
    
    #path('csv_upload/', include('page.urls')), 
    
]