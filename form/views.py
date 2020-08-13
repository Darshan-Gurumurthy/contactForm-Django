from django.shortcuts import render
from django.core.mail import send_mail
from .models import Emails
#from django.config import settings

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        #send send_mail
        send_mail(
            'Name:' + name + ' Phone number:' + phone,#subject
            message,#message
            email,#from email
            ['darshangurumurthy@gmail.com'],#to email
        )
        #save to DB also
        EmailDB = Emails(name=name,email=email,phone=phone,message=message)
        EmailDB.save()

        return render(request, 'index.html', {'name': name})


    else:
        return render(request, 'index.html', {})
