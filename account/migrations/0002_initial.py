# Generated by Django 5.0.7 on 2024-08-11 11:49

from django.db import migrations

def add_books(apps, schema_editor):
    Books = apps.get_model('account', 'Books')
    Books.objects.create(title='Азбука', author='Чапман', genre='Образование')
    Books.objects.create(title='Алгоритмы', author='Потанин', genre='Образование')
    Books.objects.create(title='Божий промысел', author='Моисей', genre='Религия')
    Books.objects.create(title='Галактический путь', author='Евсеев', genre='Приключения')

class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_books),
    ]
