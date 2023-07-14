from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
class SignInForm(AuthenticationForm):

    class Meta:
        model = CustomUser
        fields = ("email", "password")

class RegistrationForm(UserCreationForm):


    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("first_name","last_name","middle_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user























