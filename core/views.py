from django.shortcuts import render, get_object_or_404, redirect
from .models import FAQ, Product
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save form data to database
            form.save()
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
