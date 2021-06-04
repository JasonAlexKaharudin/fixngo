from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    postal_code = forms.IntegerField()
    Sign_up_as_Fixer = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'postal_code', 'Sign_up_as_Fixer']