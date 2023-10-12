from django import forms
from .models import User
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm
)

class UserRegisterForm(UserCreationForm):


    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Your password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'Your confirm password'}))
    
    class Meta:
        model = User
        fields = ['email', 'full_name', 'phone_number', 'password1', 'password2']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Your email adsress'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Your full name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': 'Your phone number'})
                                            
        }


    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError("Password and confirm password doesn't match")
        return password2
    

class UserLoginForm(AuthenticationForm):

    username = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your email'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Password'
        }))