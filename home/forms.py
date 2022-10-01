from django import forms
from home.models import Contact

class ContactForm(forms.Form):
    choices = ((1, 'Teklif'), (2, 'Irad'))
    username = forms.CharField(max_length=30, min_length=3, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Username',
    }))
    email = forms.EmailField(max_length=40, widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Email'    
    }))
    choices = forms.ChoiceField(choices=choices, widget=forms.Select(attrs={
        'class':'form-control',
    }))
    message = forms.CharField(max_length=300, widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Message'
    }))

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("username", 'email', 'subjets', 'message')

        widgets = {
            'username':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Username'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'Email'
            }),
            'subjets':forms.Select(attrs={
                'class':'form-control',
                # 'placeholder':'Username'
            }),
            'message':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Message'
            })



        }