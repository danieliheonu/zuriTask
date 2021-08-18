from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):

    if request.method == "POST":
        name = request.POST['name']
        return render(request, 'success.html', {'name': name})
    return render(request, 'index.html')
