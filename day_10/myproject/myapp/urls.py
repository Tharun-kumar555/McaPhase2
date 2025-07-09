from django.urls import path
from .views import BookCreateView, BookListView 
from .views import BookUpdateView, BookDeleteView
urlpatterns = [
    path('list/', BookListView.as_view(), name='book_list'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
]
