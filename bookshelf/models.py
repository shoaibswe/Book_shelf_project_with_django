# Create your models here.
from django.db import models
from django.utils import timezone


# Create your models here.

class booktype(models.Model):
    book_type = models.CharField(max_length=255)
    book_avail = models.CharField(max_length=255)
    book_publish = models.CharField(max_length=255)

    def __str__(self):
        return self.book_type

class books(models.Model):
    book_name = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    book_version = models.FloatField()
    book_price = models.PositiveIntegerField()
    publish_year = models.DateTimeField(default=timezone.now())
    booktype = models.ForeignKey(booktype, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name
