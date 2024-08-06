from django.http import Http404
from django.shortcuts import render

from account.models import Books, TakenBooks

from django.views import generic

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def take_book(request, book_id):
    user = request.user
    book = Books.objects.get(id=book_id)
    if not TakenBooks.objects.filter(reader_id=user.id, book_id=book.id).exists():
        TakenBooks.objects.create(reader_id=user.id, book_id=book.id)
    return redirect('books')  # Redirect back to the book list

@login_required
def return_book(request, book_id):
    user = request.user
    TakenBooks.objects.filter(reader_id=user.id, book_id=book_id).delete()
    return redirect('books')  # Redirect back to the book list

class BookListView(generic.ListView):
    model = Books

    template_name = 'reader/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['taken_books_ids'] = list(
            TakenBooks.objects.filter(reader_id=user.id).values_list('book_id', flat=True))
        return context





        # Get the context from the parent class
        # context = super().get_context_data(**kwargs)
        # # Add data from another model
        # context['taken'] = TakenBooks.objects.all()  # Assuming Authors is another model you want to include
        # return context