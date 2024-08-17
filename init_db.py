import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bible_tt.settings')
django.setup()

from django.contrib.auth.models import Group

def create_groups():
    Group.objects.get_or_create(name='Readers')
    Group.objects.get_or_create(name='Librarians')

if __name__ == '__main__':
    create_groups()
