from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse
from django.db.models import Q
import csv

#@login_required
def handler404(request, exception):
    return render(request, '404.html', status=404)

@login_required
def export_emails(request):
    contacts = Contact.objects.all()
    emails = [contact.email for contact in contacts]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="emails.csv"'

    writer = csv.writer(response)
    writer.writerow(['Emails'])
    for email in emails:
        writer.writerow([email])

    return response

@login_required
def contact_list(request):
    query = request.GET.get('q')
    contacts = Contact.objects.order_by('-date_added')[:10]

    if query:
        contacts = contacts.filter(
            Q(name__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(email__icontains=query) |
            Q(region__icontains=query) |
            Q(gender__icontains=query)
        )
    total_count = contacts.count()
    context = {
        'contacts': contacts,
        'query': query,
        'total_count': total_count
    }
    return render(request, 'contacts/contact_list.html', context)

#@login_required
def thank_you(request):
    
    return render(request, 'contacts/thank_you.html')

def thank_you_o(request):
    return render(request, 'contacts/thank_you_o.html')

#@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            phone_number = form.cleaned_data.get('phone_number')
            formatted_phone_number = '+252' + phone_number[-9:]  
            contact.phone_number = formatted_phone_number
            contact.save()
            return redirect('thank_you')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'contacts/contact_create.html', context)

@login_required
def delete_all_contacts(request):
    if request.method == 'POST':
        Contact.objects.all().delete()
        return redirect('contact_list')
    else:
        return render(request, 'contacts/delete_all_confirm.html')

@login_required
def delete_all_confirm(request):
    return render(request, 'contacts/delete_all_confirm.html')
