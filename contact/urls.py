
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('<int:contact_id>/',views.contact, name='contact'),
    path('<search/',views.search, name='search'),
    path('',views.index, name='index'),
]