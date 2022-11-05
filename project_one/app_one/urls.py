from django.conf.urls import url
from app_one import views
from django.urls import path

urlpatterns = [
    path('',views.two,name='two'),
]
