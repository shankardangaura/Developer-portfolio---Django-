from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("this is my home page (/)")
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def projects(request):
    return render(request,'projects.html')
def contact(request):
    return render(request,'contact.html')