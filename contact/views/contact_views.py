from django.shortcuts import render,get_object_or_404
from contact.models import Contact
from django.http import Http404

# Create your views here.

def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[:10]

    context = {
        'contacts' : contacts,
        'site_title': 'Contacts'
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    #single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(Contact, pk=contact_id,show=True)

    #if single_contact is None:
    #    raise Http404('Contact Not Found!')
 
    context = {
        'contact' : single_contact,
        'site_title': single_contact.first_name

    }

    return render(
        request,
        'contact/contact.html',
        context
    )