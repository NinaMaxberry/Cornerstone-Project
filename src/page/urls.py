from django.urls import path, include
from django.contrib import admin


from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage_view'),
    path('results/', views.results_view, name='results_view'),
    #path('csv_upload/', include('page.urls')), 
    
]