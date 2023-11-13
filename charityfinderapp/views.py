from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ContactForm
from .models import Charityinformation
from django.core.mail import send_mail,BadHeaderError


# Create your views here.
def index_func(request):
    return render(request, 'index.html', {})


def about_func(request):
    return render(request, 'about.html', {})


def donate_func(request):
    return render(request, 'donate.html', {})


def charity_func(request):
    charity = Charityinformation.objects.all()  # select * from table ;
    return render(request, "charityform.html", {"charity": charity})


def search_charity_func(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        charityname = Charityinformation.objects.filter(charity_name__contains=searched)
        return render(request, 'search_charity.html', {'searched': searched, 'charityname': charityname})
    else:
        return render(request, 'search_charity.html', {})


def contact_func(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            content = contact_form.cleaned_data['content']

            send_mail('The contact form subject', 'This is the message', 'ataullah.behesti@gmail.com',
                      ['ataullah.behesti@yahoo.com'])
            return redirect('contact_func')
    else:
        contact_form = ContactForm()

    return render(request, 'contact.html', {'contact_form': contact_form})


