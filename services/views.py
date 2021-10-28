from django.shortcuts import render
from .models import Service


def index(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'index.html', context)