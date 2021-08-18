from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):

    if request.method == "POST":

        send_mail(
            request.POST['subject'],
            request.POST['body'],
            request.POST['name'],
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return render(request, 'success.html')
    return render(request, 'index.html')
