from django import forms
# from django.forms import widgets, PasswordInput
from django.contrib.auth.models import User
from .models import profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input-text with-border',
        'placeholder': 'Username',
        'name': 'username',
        'id': "username",
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'required': True,
        'class': 'input-text with-border',
        'placeholder': 'EmailAddress',
        'name': 'email',
        'id': "email",
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-text with-border', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input-text with-border', 'placeholder': 'Repeat Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput({
        'class': 'input-text with-border',
        'name': 'username',
        'id': "username",
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput({
        'class': 'input-text with-border',
        'name': 'password',
        'id': "password",
        'placeholder': 'Password'
    }))


class UserUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'with-border'})
        self.fields['last_name'].widget.attrs.update({'class': 'with-border'})
        self.fields['email'].widget.attrs.update({'class': 'with-border'})

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'class': 'with-border'
        }


class ProfileUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'file-upload'})
        self.fields['intro'].widget.attrs.update({'class': 'with-border'}, rows='2')

    class Meta:
        model = profile
        fields = ('image', 'intro')
        widgets = {
            'class': 'file-upload'
        }
