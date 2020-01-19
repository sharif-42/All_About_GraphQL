from django.contrib import admin

from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_name',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'total_publication',
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'name',
        'price',
        'page',
        'published_date',
        'update_date',
    )
    list_filter = ('author', 'published_date', 'update_date')
    search_fields = ('name',)

