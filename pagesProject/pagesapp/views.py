from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomepageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactsPageView(TemplateView):
    template_name = 'contacts.html'

class ServicesPageView(TemplateView):
    template_name = 'services.html'

class PartnersPageView(TemplateView):
    template_name = 'partners.html'