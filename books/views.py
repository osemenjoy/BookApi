from .models import Books
from .serializers import BookSerializers
from rest_framework import generics
from rest_framework import viewsets, pagination, status
from rest_framework.decorators import action
from rest_framework.response import Response
from main.permissions import IsAdminOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializers
    pagination_class = pagination.PageNumberPagination  
    page_size = 20
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=True, methods=['get'], url_path='check_availability')
    def get(self, request, pk=None):
        try:
            book = Books.objects.get(pk=pk)
            available = book.available

            return Response(
                {
                    'available': available
                }, status=status.HTTP_200_OK
            )
        except Books.DoesNotExist:
            return Response(
                {
                    'error': 'Book not found'
                }, status=status.HTTP_404_NOT_FOUND
            )


class BookSearchViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializers

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title')
        author = self.request.query_params.get('author')
        isbn = self.request.query_params.get('isbn')
        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if isbn:
            queryset = queryset.filter(isbn__icontains=isbn)

        return queryset