

# Create your views here.
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Book


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'publication_date']
    template_name = 'book_form.html'  # Optional: specify custom template
    success_url = reverse_lazy('book_list')  # URL to redirect to after successful form submission

class BookListView(ListView):
    model = Book
    context_object_name = 'books'  # Optional: specify the context variable name in templates
    template_name = 'book_list.html'  # Optional: specify custom template

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_date']
    template_name = 'book_form.html'  # Optional: specify custom template
    success_url = reverse_lazy('book_list')  # URL to redirect to after successful form submission

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'  # Optional: specify custom template
    success_url = reverse_lazy('book_list')  # URL to redirect to after successful deletion