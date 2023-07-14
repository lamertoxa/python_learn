from django.contrib import admin
from .models import Book
from author.models import Author
class AuthorInLine(admin.TabularInline):
    model = Author.books.through
    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        else:
            return 1
    def has_add_permission(self, request, obj):
        return not bool(obj)
    def has_change_permission(self, request,obj=None):
        return not bool(obj)
    def has_delete_permission(self, request, obj=None):
        return not bool(obj)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name','year_of_publication','author']
        else:
            return []
    inlines = [AuthorInLine,]
    list_display = ('id', 'name', 'description', 'count', 'get_author','year_of_publication','date_of_issue')
    list_filter = ('id','name','count','authors')
    fieldsets = (
        ('Editable',{
        'fields':('date_of_issue','description','count')
                       }),('Uneditable',{'fields':('name','year_of_publication')
                                           })
    )
    @admin.display(description='author')
    def get_author(self, obj):
        return ', '.join([f"{author.name} {author.surname} {author.patronymic}" for author in obj.authors.all()])




