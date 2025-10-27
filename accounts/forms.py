from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    """Form for user registration"""
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email
