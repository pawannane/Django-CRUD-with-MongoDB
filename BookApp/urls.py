from django.conf.urls import urls
from BookApp import views

urlpatterns = [
    urls(r'^books$', views.BookApi),
    urls(r'books/([0-9]+)')
]