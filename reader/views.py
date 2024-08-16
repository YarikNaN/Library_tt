from django.http import Http404
from django.shortcuts import render
from django.utils import timezone

from account.models import Books, TakenBooks

from django.views import generic

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required, user_passes_test

# Проверка, является ли пользователь членом группы
def group_required(*group_names):
    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_names)):
                return True
        return False
    return user_passes_test(in_groups)

@login_required
@group_required('Readers')
def take_book(request, book_id):
    user = request.user
    book = Books.objects.get(id=book_id)
    if not TakenBooks.objects.filter(reader_id=user.id, book_id=book.id).exists():
        TakenBooks.objects.create(reader_id=user.id, book_id=book.id)
    return redirect('books')  # Redirect back to the book list

@login_required
@group_required('Readers')
def return_book(request, book_id):
    user = request.user
    TakenBooks.objects.filter(reader_id=user.id, book_id=book_id).delete()
    return redirect('books')  # Redirect back to the book list


class MyBooksListView(generic.ListView):
    model = TakenBooks
    template_name = 'reader/mybooks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        taken_books = TakenBooks.objects.filter(reader_id=user.id).order_by('book__title')
        now = timezone.now()
        # Добавляем количество дней в контекст
        context['taken_books_with_days'] = [
            {
                'book': taken_book.book,
                'taken_date': taken_book.taken_date,
                'days_on_hand': (now - taken_book.taken_date).days
            }
            for taken_book in taken_books
        ]
        return context

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