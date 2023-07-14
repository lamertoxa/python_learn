from django import template

register = template.Library()

def list_authors(value):
    return ', '.join([i.name for i in value.authors.all()])

def list_books(value):
    return ', '.join([i.name for i in value.books.all()])

register.filter('list_authors',list_authors)

register.filter('list_books',list_books)