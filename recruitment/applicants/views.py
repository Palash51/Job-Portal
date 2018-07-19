#import all the necessary built-in modules and required modules from other files.
from django.shortcuts import render, redirect
from django.conf import settings
from recruitment.applicants.models import Document
from recruitment.applicants.forms import DocumentForm
from django.views.generic import FormView, CreateView
from django.core.urlresolvers import reverse, reverse_lazy, resolve



# def home(request):
#     """
#     Function based views which returns home page/landing page of the application.

#     """
#     documents = Document.objects.all()
#     return render(request, 'applicants/home.html', { 'documents': documents })


class HomePageView(FormView):
    template_name = 'applicants/home.html'
    form_class = DocumentForm


# def registration(request):
#     """
#     Function which will validate form as well as allow users to upload files
#     and save it to db if and only if form is validate else it will return to registration page.
#     """
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return render(request, 'applicants/success.html')
#     else:
#         form = DocumentForm()
#     return render(request, 'applicants/registration.html', {
#         'form': form
#     })


class RegistrationView(CreateView):
    #template_name = 'applicants/'
    form_class = DocumentForm
    model = Document
    #D = Document.objects.get().Name
    #Document = Document.objects.all()[0]
    #model = Document
    success_url = reverse_lazy('applicants/success')
    template_name = 'applicants/registration.html'


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()
        return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    #def form_valid(self, form):

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            import pdb
            pdb.set_trace()

            #return self.form_valid(form, **kwargs)
            return render(request, 'applicants/success.html',)
        else:
            return self.form_invalid(form, **kwargs)


    # def get_context_data(self, request, *args, **kwargs):
    #     context = {
    #     'qs' : Document.objects.all()
    #     }
    #     return render(request, 'applicants/success.html', context)


    # def form_valid(self, form):
    #     user = form.save(commit=False)
    #     if form.is_valid():
    #         #return self.form_valid(form, **kwargs)
    #         return render(self.request, 'applicants/success.html')
    #     else:
    #         return self.form_invalid(form, **kwargs)
        
        