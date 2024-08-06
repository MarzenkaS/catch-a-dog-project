from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('contact:success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def success_view(request):
    return render(request, 'contact/success.html')
