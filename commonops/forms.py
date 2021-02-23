from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('full_name', 'email', 'phone_number')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('full_name', 'email', 'phone_number')




class LoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class ChangePassForm(forms.Form):
    email = forms.EmailField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'col-sm-5', 'placeholder': 'Email Address'}))
