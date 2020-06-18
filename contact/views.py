from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from contact.forms import ContactForm
# Create your views here.
def send_email(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            from_email = form.cleaned_data.get('from_enail')
            message = form.cleaned_data.get('message')
            try:
                send_mail(subject,message,from_email,['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid Header')
            return redirect('success')
    else:
        form = ContactForm()
    context = {
        "form": form
    }
    return render(request, 'contact/contact.html', context)

def send_success(request):
    return HttpResponse("Thank You! For Contacting Us")    