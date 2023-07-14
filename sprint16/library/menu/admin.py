from django.contrib import admin
from authentication.models import CustomUser
from book.models import Book
from author.models import Author
from order.models import Order


class AuthorInline(admin.TabularInline):
    model = Author.books.through

    def has_change_permission(self, request, obj=None):
        return not bool(obj)

    def has_add_permission(self, request, obj=None):
        return not bool(obj)

    def has_delete_permission(self, request, obj=None):
        return not bool(obj)


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name', 'email', 'role', 'is_staff', 'is_superuser', 'created_at', 'updated_at', )
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('id', 'first_name', 'middle_name', 'last_name', 'email')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author_name', 'description', 'count', 'year_of_publication', 'date_of_issue')
    list_filter = ('id', 'name', 'authors')
    search_fields = ('id', 'name', 'description')

    fieldsets = (
        ('Main information', {'fields' : ('name', 'description', 'year_of_publication')}),
        ('Changeable info', {'fields': ('count', 'date_of_issue')}),
    )

    inlines = [AuthorInline]

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name', 'description', 'year_of_publication']
        else:
            return []

    @admin.display(description='authors\' names')
    def author_name(self, my_book):
        return ", ".join([f"{i.name} {i.surname} {i.patronymic}" for i in my_book.authors.all()]) \
               or "Please add authors"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic')
    search_fields = ('id', 'name', 'surname', 'patronymic')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name', 'surname', 'patronymic']
        else:
            return []


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'book', 'created_at', 'end_at', 'plated_end_at')
    search_fields = ('id', 'user', 'book')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['user', 'book', 'created_at']
        else:
            return []


