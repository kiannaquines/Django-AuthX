from django import forms
from django.contrib.auth import get_user_model
from .models import AuthXUserModel
from django.contrib.auth.forms import UserCreationForm

class AuthXLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        ),
        help_text='Enter your username',
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        ),
        help_text='Enter your password',
        required=True
    )

class AuthXRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(AuthXRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = AuthXUserModel
        fields = ['username','email',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username