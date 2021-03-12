from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('booklist/', views.BookListView.as_view(),name='book_list'),
    path('bookcreate/',views.BookCreateView.as_view(),name='book_create'),
    path('book/<int:pk>/detail/', views.BookRetrieveView.as_view(), name='book_retrieve'),
    path('book/<int:pk>/delete/',views.BookDestroyView.as_view(),name='book_destroy'),
    path('book/<int:pk>/update/',views.BookUpdateView.as_view(),name='book_update')
]

urlpatterns = format_suffix_patterns(urlpatterns)