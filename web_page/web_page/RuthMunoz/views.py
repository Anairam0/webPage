import re
from datetime import datetime
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    now = datetime.now()

    formatted_now = now.strftime("%A. %d %b, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name +"! Its " + formatted_now
    return HttpResponse(content)