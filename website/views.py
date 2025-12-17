from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def index_view(request):
    return render(request,'website/index.html')


# Create your views here

def index(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
        messages.success(request, "Your message has been sent. Thank you!")
        return redirect("/")

    return render(request, "website/index.html") 
