from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            'full_name',
            'phone_number',
            'email',
        ]


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class ChangePassForm(forms.Form):
    email = forms.EmailField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'col-sm-5', 'placeholder': 'Email Address'}))
