from django.contrib import admin

# Register your models here.

from .models import Room


# Đăng kí UI qli Room trong admin panel
admin.site.register(Room)