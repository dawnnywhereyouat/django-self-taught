from django.contrib import admin

# Register your models here.

from .models import *


# Đăng kí UI qli Room trong admin panel
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)