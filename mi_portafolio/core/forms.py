from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['nombre','email','asunto','mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'required': True, 'minlength': 2}),
            'email': forms.EmailInput(attrs={'required': True}),
            'mensaje': forms.Textarea(attrs={'required': True, 'minlength': 10}),
        }
