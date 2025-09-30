from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Project, FAQ, OpenItem
from .forms import ContactForm
from django.urls import reverse

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()
    return render(request,'home.html',{'profile':profile,'projects':projects})

def contactame(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('contact_success'))
    else:
        form = ContactForm()
    return render(request,'contactame.html',{'form':form})

def contact_success(request):
    return render(request,'contact_success.html')

def fyq(request):
    faqs = FAQ.objects.all()
    return render(request,'fyq.html',{'faqs':faqs})

def open_list(request):
    items = OpenItem.objects.all()
    return render(request,'open.html',{'items':items})

def open_detail(request, pk):
    item = get_object_or_404(OpenItem, pk=pk)
    return render(request,'open_detail.html',{'item':item})
