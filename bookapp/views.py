from common.utils import string_to_bool
from rest_framework import viewsets

from .filtersets import BookListOrFilter, BookListAndFilter
from .serializers import BookSerializer
from .models import Book

import ast


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    """
    A view that list, update, delete, create book.
    It can be paginated, searchable and filterable by multiple genres.
    """
    queryset = Book.objects
    serializer_class = BookSerializer
    filterset_fields = ['genere']
    filterset_class = BookListOrFilter
    search_fields = ['synopsis', 'name', 'author']

    def get_queryset(self):
        """
        If there is 'and' query parmeter is specified as true , we does AND operator for the genere filters.
        """
        is_and_operator = self.request.query_params.get('and', 'false')
        is_and_operator = string_to_bool(is_and_operator)
        if is_and_operator:
            self.filterset_class = BookListAndFilter
        return super().get_queryset()
