from django.urls import path
from .views import index, new_contact, service_detail

app_name = 'services'
urlpatterns = [
    path('contact_new/', new_contact, name='contact_new'),
    path('<service_slug>/', service_detail, name='service_detail'),
    path('', index, name='index'),
]