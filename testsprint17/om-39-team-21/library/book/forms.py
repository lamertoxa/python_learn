from .models import Book
from django.forms import ModelForm
from django import forms
from author.views import Author


class DateInput(forms.DateInput):
    input_type = "date"

class BookForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.name:
            self.fields['name'].widget.attrs['readonly'] = True

    class Meta:
        model = Book
        fields = ('name', 'description', 'count', 'year_of_publication', 'date_of_issue')

        widgets = {
            'date_of_issue': DateInput(),
        }


class BookAuthorForm(forms.Form):

    book_author = forms.ModelMultipleChoiceField(
        label='Author', required=False, queryset=Author.objects.all()
    )
