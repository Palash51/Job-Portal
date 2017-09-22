from django.shortcuts import render, redirect
from django.conf import settings
from recruitment.applicants.models import Document
from recruitment.applicants.forms import DocumentForm


def home(request):
    documents = Document.objects.all()
    return render(request, 'applicants/home.html', { 'documents': documents })



def registration(request):
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
