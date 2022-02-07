from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def index(request):
    if request.method == 'POST':
        message_name = request.POST.get('nombre')
        message_email = request.POST.get('email')
        message = request.POST.get('texto')
        # send an email
        send_mail(
        "message from " +message_name+ ", Email: "+message_email, #Subject
        message, #Message)
        message_email, # from message_email
        ['pablocfes@gmail.com'])
        return render(request, 'index.html',{'message_name': message_name})

    else:
        return render(request, 'index.html',)
    

