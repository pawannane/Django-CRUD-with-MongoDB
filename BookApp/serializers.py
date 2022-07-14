from rest_framework import serializers
from BookApp.models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Books 
        fields=('BookId','BookName','Quantity','BookGenre','IsBestSeller', 'CreatedAt', 'UpdatedAt')