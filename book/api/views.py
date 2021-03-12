from django.shortcuts import render
from .serializers import BookSerializer
from .models import Books
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import viewsets, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView


class BookModelViewSet(viewsets.ModelViewSet):
    search_fields = ['author','book_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookListView(ListAPIView):
    search_fields = ['author','book_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class BookCreateView(CreateAPIView):
    serializer_class = BookSerializer
    search_fields = ['author','book_name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


class BookRetrieveView(RetrieveAPIView):
    search_fields = ['author','book_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


class BookDestroyView(DestroyAPIView):
    search_fields = ['author','book_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Books.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]


class BookUpdateView(UpdateAPIView):
    search_fields = ['author','book_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]
