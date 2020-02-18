from django import forms
from ekkoUsers.models import  *
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = RegisteredUser
        fields = ["name", "email", "password", "confirm_password"]
        
        widgets = {
        'password': forms.PasswordInput(),
    }