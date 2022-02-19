# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from django.db import models
from django import forms
from django.forms import TextInput, Textarea, CharField


class CustomUserAdmin(UserAdmin):

    model = CustomUser
    list_display = ['email', 'username', 'first_name',
                    'is_active', 'is_staff']
    search_fields = ('email', 'username')
    list_filter = ('email', 'username', 'first_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )
admin.site.register(CustomUser, CustomUserAdmin)
