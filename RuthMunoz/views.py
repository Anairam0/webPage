import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,"RuthMunoz/cv-ruth.html",
        {   'name': name,
            'date': datetime.now()
        }
    )