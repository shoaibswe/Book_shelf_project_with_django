from django.shortcuts import render, redirect
from .models import books,booktype


# Create your views here.


def booksview(request):
    obj = books.objects.all()
    return render(request, 'bookindex.html', {'x': obj})


def deletebook(request, id):
    book = books.objects.get(pk=id)
    book.delete()
    obj = books.objects.all()
    return redirect("/book/")

def editbook(request,id):
   # book = books.objects.get(pk=id)
    pass