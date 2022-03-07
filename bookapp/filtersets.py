import django_filters
from .models import Book, GenreList

class BookListOrFilter(django_filters.FilterSet):
    genere = django_filters.MultipleChoiceFilter(choices=GenreList.choices, lookup_expr="contains")
    class Meta:
        model = Book
        fields = ['genere']


class BookListAndFilter(django_filters.FilterSet):
    genere = django_filters.MultipleChoiceFilter(choices=GenreList.choices, lookup_expr="contains", conjoined=True)
    class Meta:
        model = Book
        fields = ['genere']
