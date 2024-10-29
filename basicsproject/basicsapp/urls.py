from tkinter.font import names

from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home,  name="Home"),
    path("yahoo", views.ShowMoreMessage,  name="Yahoo"),
    path("useVars", views.UseVariableAsResponse, name="Variables"),
    path("getTest", views.GetRequestVars, name = "get")
]