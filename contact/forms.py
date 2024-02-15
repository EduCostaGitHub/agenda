from django import forms
from contact.models import Contact
from typing import Any
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )
        widgets = {
            'first_name': forms.PasswordInput()
        }

    def clean(self) -> dict[str, Any]:
        cleaned_data= self.cleaned_data
        print(cleaned_data)
        return super().clean()