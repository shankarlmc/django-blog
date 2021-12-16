from django import forms
from django.contrib.auth.models import User

class updateUserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))
    email = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','username']
