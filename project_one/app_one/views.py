from django.shortcuts import render
from django.http import HttpResponse
from app_one.models import Topic, Webpage, AccessRecord
# Create your views here.

def one(request):
    webpages_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_records" : webpages_list}
    return render(request,'app_one/one.html',context = date_dict)

def two(request):
    return HttpResponse("HELLO WORLD")

def help(request):
    return HttpResponse("HELP")
