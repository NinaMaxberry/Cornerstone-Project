from django.urls import path, include
from django.contrib import admin


from . import views

app_name = 'page'
urlpatterns = [
    path('', views.homepage_view, name='homepage_view'),
    path('rep/', views.repList_view, name='repList_view'),
    path('zip/', views.zipUser_view, name = 'zipUsercd'),
    path('results/', views.results_view, name='results_view'),

    
]