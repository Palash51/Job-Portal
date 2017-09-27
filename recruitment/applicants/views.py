#import all the necessary built-in modules and required modules from other files.
from django.shortcuts import render, redirect
from django.conf import settings
from recruitment.applicants.models import Document
from recruitment.applicants.forms import DocumentForm


def home(request):
    """
    Function based views which returns home page/landing page of the application.

    """
    documents = Document.objects.all()
    return render(request, 'applicants/home.html', { 'documents': documents })



def registration(request):
    """
    Function which will validate form as well as allow users to upload files
    and save it to db if and only if form is validate else it will return to registration page.
    """
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'applicants/success.html')
    else:
        form = DocumentForm()
    return render(request, 'applicants/registration.html', {
        'form': form
    })
