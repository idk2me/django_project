from django.shortcuts import render


# Create your views here.
# create an index view

def index(request):
    return render(request, 'index.html')
