from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from contact.models import Contact
from typing import Any, Mapping
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'classse-A',
    #             'placeholder':'Write your first name'
    #         }
    #     )
    # )
    first_name = forms.CharField(
        help_text='help Text',
        widget=forms.TextInput(
            attrs={                
                'placeholder':'Write your first name'
            }
        ),
        label='First Name',
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['phone'].widget.attrs.update({
            'placeholder':'your phone number'
        })

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
        )
        widgets = {            
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': "Write your last name"
                }
            )
        }

    def clean(self) -> dict[str, Any]:
        cleaned_data= self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            error_msg = ValidationError(
                    'first name canot be the same that last name',
                    code='invalid',
                )
            self.add_error('first_name',error_msg)
            self.add_error('last_name',error_msg)

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro 2',
        #         code='invalid'
        #     )
        # )
        return super().clean()
    
    def clean_first_name(self):
        data = self.cleaned_data["first_name"]

        if data == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Do not input ABC',
                code='invalid'
                )                
            )
        
        return data
    