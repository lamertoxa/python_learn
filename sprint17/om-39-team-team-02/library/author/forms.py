from django import forms
from django.forms import ModelForm
from .models import Author


class AuthorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.name:
            self.fields['name'].widget.attrs['readonly'] = True
        if instance and instance.patronymic:
            self.fields['patronymic'].widget.attrs['readonly'] = True

    class Meta:
        model = Author
        fields = ('name', 'surname', 'patronymic', 'books')
        labels = {
            'name': 'Author\'s name',
            'surname': 'Author\'s surname',
            'patronymic': 'Author\'s patronymic',
            'books': 'Author\'s books',
        }
