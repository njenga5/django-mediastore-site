from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
    date_of_birth = forms.DateField(input_formats=["%Y-%m-%d", ], help_text="Enter date in form of YYYY-MM-DD.")
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'phone_number',
            'email',
        ]


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class ChangePassForm(forms.Form):
    email = forms.EmailField(max_length=50)
