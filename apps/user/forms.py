from django import forms 
from .models import User

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = {
            'username': "",
            'password': "",
            'first_name': "", 
            'last_name': "",
            'email': "",
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Username'}),
            'password': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Password'}),
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}), 
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'example@e-mail.com'}),
        }
        