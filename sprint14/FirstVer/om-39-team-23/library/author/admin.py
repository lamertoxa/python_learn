from django.contrib import admin
from .models import Author



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic','get_books')
    list_filter = ('name','surname','patronymic')
    fieldsets = (
        (None,{
        'fields':('name','surname','patronymic')
                       }),('Availability',{'fields':('books',)
                                           })
    )

    @admin.display(description='Books')
    def get_books(self, obj):
        return ', '.join([f"{book.name}" for book in obj.books.all()])

