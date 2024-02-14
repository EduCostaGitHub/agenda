from typing import Any
from django.shortcuts import render,get_object_or_404, redirect
from contact.models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )

    def clean(self) -> dict[str, Any]:
        cleaned_data= self.cleaned_data
        print(cleaned_data)
        return super().clean()

# Create your views here.

def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)        
        }
        return render(
            request,
            'contact/create.html',
            context
        )  
     
    context = {
            'form': ContactForm()        
        }
    return render(
        request,
        'contact/create.html',
        context
    )   
    

    

    
