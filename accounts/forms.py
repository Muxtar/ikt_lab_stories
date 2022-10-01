from dataclasses import fields
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password',
        'class':'form-control'
    }))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

        widgets = {
            'first_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'First Name'
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Last Name'
            }),
            'username':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Username'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Email'
            }),
            'password':forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'Password'
            })
        }

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        print(password, confirm_password)
        return super().clean()