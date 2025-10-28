from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def show_info(request):
    return HttpResponse("<h2>11256031<br>范兆東</h2>")