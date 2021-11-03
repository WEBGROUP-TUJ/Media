from django.shortcuts import render, redirect
from .models import Service, Category
from .forms import ContactRequestForm
from django.core.mail import send_mail


def index(request):
    services = Service.objects.all()
    categories = Category.objects.all()[:9]
    contact_form = ContactRequestForm()
    context = {'services': services, 'categories': categories, 'contact_form': contact_form}
    return render(request, 'index.html', context)


def new_contact(request):
    """Create new contact form"""
    if request.method == "POST":
        form = ContactRequestForm(data=request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            email_address = contact.email
            subject = 'Contact request'
            message = "Thank you for leaving request. We will contact you soon"
            send_mail(subject, message, 'mediamind@gmail.com', [email_address])
            contact.save()
            return redirect('services:index')


def service_detail(request, service_slug):
    service = Service.objects.get(slug=service_slug)
    categories = Category.objects.all()[:10]
    last_services = Service.objects.all()
    context = {'service': service, 'categories': categories, 'last_services': last_services}
    return render(request, 'service_detail.html', context)