from django import urls
from django.conf.urls import include
from django.urls import path
from django.urls.resolvers import URLPattern
from basic_app import views
from django.conf.urls import url

# TEMPLATE TAGGING
app_name = "basic_app"

urlpatterns = [
    path('',views.index,name='index'),
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]