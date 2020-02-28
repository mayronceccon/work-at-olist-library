from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    ordering = ('-name',)
    fields = ('name',)
    list_display = ['name']


admin.site.register(Author, AuthorAdmin)
