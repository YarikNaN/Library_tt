from django.urls import path
import reader.views

urlpatterns = [

    path('take_book/<int:book_id>/', reader.views.take_book, name='take_book'),
    path('return_book/<int:book_id>/', reader.views.return_book, name='return_book'),

]


