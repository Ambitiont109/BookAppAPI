from django.db.models import fields
from rest_framework import serializers
from .models import Book,GenreList


class BookSerializer(serializers.ModelSerializer):
    genere = serializers.ListField(
        child=serializers.ChoiceField(
            choices=GenreList.choices,
            allow_blank=False),
        write_only=True,
    )
    generes = serializers.CharField(source="genere", read_only=True)
    class Meta:
        model = Book
        fields = '__all__'