from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'phone_number',
            'email',
        ]
        attrs = {'class': 'form-control'}
        widgets = {
            'first_name': forms.TextInput(attrs),
            'middle_name': forms.TextInput(attrs),
            'last_name': forms.TextInput(attrs),
            'phone_number': forms.TextInput(attrs),
            'email': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
        }


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class ChangePassForm(forms.Form):
    email = forms.EmailField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'col-sm-5', 'placeholder': 'Email Address'}))
