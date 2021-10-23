from django.urls import path
from .views import index

app_name = 'services'
urlpatterns = [
    path('', index, name='index'),
]