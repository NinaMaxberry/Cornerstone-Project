from django.urls import include, path
from django.contrib import admin




from page import views

app_name = 'page'

urlpatterns = [
    
    path('home/', views.homepage_view, name='homepage_view'),
    path('results/', views.results_view, name='results_view'),

]