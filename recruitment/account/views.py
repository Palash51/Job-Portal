from __future__ import unicode_literals

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseForbidden, HttpResponse

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView

from recruitment.account.forms import RegisterUserForm, LoginForm
#from account.models import Registration


from django.contrib.auth import logout
from django.views.generic import RedirectView

from django.core.mail import send_mail


# def home(request):
#     return render(request, 'account/home.html')

class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "account/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()

        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        # email = form.cleaned_data['email']
        # Subject = 'Welcome'
        # from_email = settings.EMAIL_HOST_USER
        # to_email = [from_email, 'palashpatidar51@gmail.com']
        # contact_message = "%s hello %s"% (user,email)
        # send_mail = (Subject,
        #             contact_message,
        #             from_email,
        #             to_email)
        user.save()
        return render(self.request, 'account/welcome.html', {'form': form})
        #return HttpResponse('User registered')


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = "account/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')


# class LogoutView(LogoutView):
#     template_name = 'applicants/home.html'


class LogoutView(RedirectView):
    """
    A view that logout user and redirect to homepage.
    """
    permanent = False
    query_string = True
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        """
        Logout user and redirect to target url.
        """
        if self.request.user.is_authenticated():
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)





@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'account/dashboard.html'
    
    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)
