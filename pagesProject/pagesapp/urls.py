from django.urls import path
from .views import HomepageView, AboutPageView, ContactsPageView, ServicesPageView, PartnersPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('',HomepageView.as_view(),name='home'),
    path('contacts/', ContactsPageView.as_view(), name='contacts'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('partners/', PartnersPageView.as_view(), name='partners')

]