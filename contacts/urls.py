from django.urls import path
from contacts.views import contact_list, contact_create, thank_you, export_emails, delete_all_contacts, delete_all_confirm, thank_you_o

urlpatterns = [
    path('contact_list', contact_list, name='contact_list'),
    path('', contact_create, name='contact_create'),
    path('contacts/thank-you/', thank_you, name='thank_you'),
    path('contacts/thank-you_o/', thank_you_o, name='thank_you_o'),
    path('contacts/export-emails/', export_emails, name='export_emails'), 
    path('delete_all/', delete_all_contacts, name='delete_all_contacts'),
    path('delete_all/confirm/', delete_all_confirm, name='delete_all_confirm'),

]
