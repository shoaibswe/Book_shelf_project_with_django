from django.urls import path
from . import views
urlpatterns = [
    path('', views.booksview, name='books'),
    path('edit/<id>/', views.editbook, name='editbook'),
    path('delete/<id>/', views.deletebook, name='deletebook'),
]
