from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group
from .models import Register

# Register your models here.
# admin.site.unregister(Register)

admin.site.register(Register)
# admin.site.unregister(Group)
