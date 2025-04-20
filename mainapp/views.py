from django.shortcuts import render,HttpResponse
from .models import ContactMessage
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

def index(request):
    # Handle only normal GET request for initial load
    return render(request, 'index.html')
    
@csrf_exempt
def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            # Save to database
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            # Send email to yourself
            send_mail(
                subject=f'New Contact Form Submission: {subject}',  # Email subject
                message=f'From: {name} <{email}>\n\nMessage:\n{message}',  # Email body
                from_email='yeolekrushna00@gmail.com',  # Sender (must match EMAIL_HOST_USER)
                recipient_list=['yeoleagency@gmail.com'],  # Who receives the email
                fail_silently=False  # Raise error if it fails
            )

            return HttpResponse("success")

    return HttpResponse("failed")


def work(request):
    return render(request, 'work.html')
