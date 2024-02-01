from django.shortcuts import render
from django.views import generic
from models import Book


# Create your views here.
# create an index view

def index(request):
    return render(request, 'index.html')


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
