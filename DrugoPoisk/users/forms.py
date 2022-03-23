from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'real_name', 'city', 'birth')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'real_name', 'city', 'birth')


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', max_length=100, min_length=5,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
