from django.forms import ModelForm
from django import forms
from .models import Order


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Order
        fields = ('book', 'user', 'plated_end_at')
        labels = {
            'book': 'Select book',
            'user': 'Select user',
            'plated_end_at': 'Planned end time',
        }

        widgets = {
            'plated_end_at': DateTimeInput(),
        }

