import logging
from django import forms
from .models import Book
from author.models import Author

FILTER_SEARCH =(
    ("1", "Title"),
    ("2", "Author name"),
    ("3", "Description"),

)
class FilterSearchForm(forms.Form):
    filter_search = forms.ChoiceField(choices=FILTER_SEARCH)

class ChangeBookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        authors = kwargs.pop('authors')
        choices = kwargs.pop('choices')
        choices = [(i.id, i.name) for i in choices]
        logging.warning(f"{choices}")
        super(ChangeBookForm, self).__init__(*args, **kwargs)
        self.fields['authors'].queryset = authors
        self.fields['authors'].select = choices

    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ("count", "date_of_issue", "description", "name", "year_of_publication","authors")







