from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import FAQ, Product
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save form data to database
            contact_instance = form.save()
            # Send email
            subject = f'Nuevo mensaje de contacto de {contact_instance.name}'
            message = f'Nombre: {contact_instance.name}\nEmail: {contact_instance.email}\nMensaje: {contact_instance.message}'
            from_email = settings.EMAIL_HOST_USER
            to_email = [settings.EMAIL_HOST_USER]  # Send to yourself
            try:
                send_mail(subject, message, from_email, to_email)
            except Exception as e:
                # Log error or handle
                pass  # For now, ignore email errors
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contactame.html', {'form': form})

def fyq(request):
    faqs = FAQ.objects.all()
    return render(request, 'fyq.html', {'faqs': faqs})

def open_view(request):
    products = Product.objects.all()
    return render(request, 'open.html', {'products': products})

def open_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'open_detail.html', {'product': product})

def contact_success(request):
    return render(request, 'contact_success.html')
