from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path("",views.index, name= 'home'),
    path("home/",views.index, name= 'home'),
    path('work/', views.work, name='work'),
    path('submit-contact/', views.submit_contact, name='submit_contact'),

]
