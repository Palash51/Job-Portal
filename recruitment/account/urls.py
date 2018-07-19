from django.conf.urls import url
from django.contrib.auth.views import LogoutView
from recruitment.account import views
from recruitment.account.views import RegisterUserView, LoginUserView, DashboardView


urlpatterns = [
    # /account/register
    #url(r'^home/$', views.home, name='home'),
    url(r'^register/$', view=RegisterUserView.as_view(), name='register'),
    url(r'^login/$', view=LoginUserView.as_view(), name='login'),
    url(r'^logout/$', view=LogoutView.as_view(), name='logout'),
    url(r'^dashboard/$', view=DashboardView.as_view(), name='dashboard')
]