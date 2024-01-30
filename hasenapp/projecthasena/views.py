from django.http.response import HttpResponse
from django.shortcuts import render



#create your views here.
def index(request):
    return render (request, "projecthasena/index.html")

def blogs(request):
     return render (request, "projecthasena/blogs.html")

def blog_details(request, id):
    return render ("blog_details.html", {
        "id":id
    })
