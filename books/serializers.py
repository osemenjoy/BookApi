from rest_framework import serializers
from .models import Books

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('id', 'title', 'author', 'isbn', 'publication_date', 'available',)


    def validate_isbn(self, value):
        if len(value) not in [10, 13]:
            raise serializers.ValidationError("ISBN is either 10 or 13 characters long")
        return value
