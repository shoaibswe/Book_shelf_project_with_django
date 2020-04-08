from django.shortcuts import render

from .models import books
# Create your views here.


def booksview(request):
    obj = books.objects.all()
    return render(request, 'bookindex.html', {'x': obj})
