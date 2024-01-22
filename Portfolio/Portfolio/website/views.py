from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from .models import storeDetails

def home(request):
    return render(request, 'website/home.html')


def about(request):
    return render(request, 'website/about.html')


def projects(request):
    return render(request, 'website/projects.html')


def contact(request):
    confirmation_message = None  # Initialize confirmation_message so it can be passed to the template even
    # if the method is not post for form

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(sender_name, sender_email, message)

            # Info saved to database
            contact_details=storeDetails(name=sender_name,email=sender_email,message=message)
            contact_details.save()

            send_mail(
                'Subject of the Email',
                f'Name: {sender_name}\nEmail: {sender_email}\n\n{message}',
                sender_email,
                ['uvs2111@gmail.com'],  # Replace with your email
                fail_silently=False,
            )
            confirmation_message = "Thank you for contacting ! You'll hear soon."
            form = ContactForm()  # Reset form after successful submission
    else:
        form = ContactForm()

    return render(request, 'website/contact.html', {'form': form, 'confirmation_message': confirmation_message})


def experience(request):
    return render(request, 'website/experience.html')
