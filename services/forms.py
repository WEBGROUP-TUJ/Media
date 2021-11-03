from django import forms
from .models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'phone']
        labels = {'name': "", 'email': "", 'phone': ""}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше полное имя *'}),
                   'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваша электронная почта *'}),
                   'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш номер телефона *'})}