from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'klitchka', 'email', 'city', 'birth', 'gender')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'klitchka', 'email', 'city', 'birth', 'gender')


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', max_length=100, min_length=5,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# Для профиля СТАРТ
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'klitchka', 'email', 'city', 'birth', 'gender')


class ChangeProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'klitchka',
            'email',
            'city',
            'birth',
            'gender',
            'password'
        )