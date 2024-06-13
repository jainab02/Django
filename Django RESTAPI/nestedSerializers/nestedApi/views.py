from django.shortcuts import render
from nestedApi.models import Author, Book
from nestedApi.serializers import BookSerializer,AuthorSerializer
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from rest_framework import generics

# Create your views here.

class BookPaginaton(LimitOffsetPagination):
    page_size=2 


class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [BasicAuthentication ]
    permission_classes=[IsAuthenticated,DjangoModelPermissions]


    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['rating']

class AuthorDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
