from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# =====
# Function based Views
# =====
def Home(request):
    return HttpResponse("<h1>Hello World!!</h1>")
