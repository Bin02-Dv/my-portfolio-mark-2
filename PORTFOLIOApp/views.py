from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ContactMe

# Create your views here.

def index(request):
    return render(request, 'index.html')

def contactme(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        if len(name) < 2:
            return JsonResponse({
                "success": False,
                "message": 'Your Fullname is REQUIRED please'
            })
        elif len(email) < 3:
            return JsonResponse({
                "success": False,
                "message": "Your Email is REQUIRED please"
            })
        else:
            new_contact = ContactMe.objects.create(
                name=name, email=email, subject=subject, message=message
            )
            new_contact.save()
            return JsonResponse({
                "success": True,
                "message": "Your Message is sent SUCCESSFUL.."
            })
    return redirect("/")
