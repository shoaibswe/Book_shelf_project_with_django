from django.contrib import admin
from .models import books, booktype

# Register your models here.
class myBookView(admin.ModelAdmin):
    list_display = ('book_name', 'book_author', 'book_price', 'book_version')


admin.site.register(books, myBookView)
admin.site.register(booktype)
