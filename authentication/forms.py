from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import TextInput

# class registerUserForm(forms.ModelForm):
#     first_name = forms.CharField(
#         max_length=100,
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )
#     last_name = forms.CharField(
#         max_length=100,
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )
#     username = forms.CharField(
#         max_length=100,
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )
#     email = forms.CharField(
#         max_length=100,
#         required=True,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )
#     password1 = forms.CharField(
#         max_length=254,
#         required=True,
#         widget=forms.PasswordInput(
#             attrs={
#                 'class':'form-control'
#             }
#         )
#     )

#     password2 = forms.CharField(
#         max_length=254,
#         required=True,
#         widget=forms.PasswordInput(
#             attrs={
#                 'class':'form-control'
#             }
#         )
#     )
    
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name','email','username','password1','password2']

class updateUserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    email = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','username']
