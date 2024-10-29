from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# =====
# Function based Views
# =====
def Home(request):
    return HttpResponse("<h1>Hello World!!</h1>")

def ShowMoreMessage(request):
    return HttpResponse("" +
                        "<h1>Hello World!!</h1>" +
                        "<h2>Yahooooo!!</h2>" +
                        "")

def UseVariableAsResponse(request):
    Message = "<h1>Welcome</h1>"
    return HttpResponse(Message)

def GetRequestVars(request):
    if(request.method == "GET"):
        if(request.GET.get("Message")):
            Message = request.GET.get("Message")
        else:
            Message = "<h1>Should be GET</h1>"
    return HttpResponse(Message)