from django import forms
from .models import Contact

class Form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'address', 'category']
