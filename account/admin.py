from django.contrib import admin

# Register your models here.


from django.contrib.auth.admin import UserAdmin

from account.models import Reader

admin.site.register(Reader, UserAdmin)
