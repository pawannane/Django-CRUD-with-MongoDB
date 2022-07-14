from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BookApp.models import Books
from BookApp.serializers import BooksSerializer

from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def BookApi(request, id=0):
    if request.method == 'GET':
        Books = Books.objects.all()
        Books_serializer = BooksSerializer(Books, many=True)
        return JsonResponse(Books_serializer.data, safe=False)
    elif request.method == 'POST':
        books_data = JSONParser().parse(request)
        Books_serializer = BooksSerializer(data=books_data)
        if Books_serializer.is_valid():
            Books_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        books_data = JSONParser().parse(request)
        books = Books.objects.get(booksId=books_data['BookId'])
        Books_serializer = BooksSerializer(books, data=books_data)
        if Books_serializer.is_valid():
            Books_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        books = Books.objects.get(BookId=id)
        books.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
