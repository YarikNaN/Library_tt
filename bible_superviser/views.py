from django.http import Http404
from django.shortcuts import render
from django.utils import timezone

from account.models import Books, TakenBooks, Reader

from django.views import generic

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

class UsersListView(generic.ListView):
    model = Reader
    template_name = 'bible_superviser/spisok.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()

        # Словарь для хранения данных по каждому пользователю
        readers_with_books = []

        # Получаем всех пользователей
        readers = Reader.objects.all()

        for reader in readers:
            # Получаем все взятые книги для каждого пользователя
            taken_books = TakenBooks.objects.filter(reader_id=reader.user_id).order_by('book__title')

            # Собираем информацию по каждой книге
            taken_books_with_days = [
                {
                    'book': taken_book.book,
                    'taken_date': taken_book.taken_date,
                    'days_on_hand': (now - taken_book.taken_date).days
                }
                for taken_book in taken_books
            ]

            # Добавляем данные по пользователю и его книгам в список
            readers_with_books.append({
                'reader': reader,
                'taken_books_with_days': taken_books_with_days
            })

        # Передаем данные в контекст
        context['readers_with_books'] = readers_with_books
        return context



# class UsersListView(generic.ListView):
#     # model = Reader
#     template_name = 'reader/mybooks.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         now = timezone.now()
#         readers = Reader.objects.all()
#
#


















class BookListView(generic.ListView):
    model = Books

    template_name = 'reader/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['taken_books_ids'] = list(
            TakenBooks.objects.filter(reader_id=user.id).values_list('book_id', flat=True))
        return context



