from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):

  my_context = {
    "my_text" : "This is home page",
    "my_number" : 123,
    "my_list" : [1,2,3,4,5,6,7,8,9,10]
  }

  return render(request, "home.html", my_context)