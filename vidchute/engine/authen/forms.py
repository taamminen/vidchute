from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)
        labels = {'first_name': '', 'last_name': '', 'email': '', 'password': ''}
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Username'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-mail'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }
