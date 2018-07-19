
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from recruitment.applicants import views
from recruitment.applicants.views import HomePageView
from recruitment.applicants.models import Document



urlpatterns = [
    #url(r'^$', views.home, name='home'),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^recruitment/form/$', views.RegistrationView.as_view(), name='registration'),
    #url(r'^recruitment/form/$', views.registration, name='registration'),
    url(r'^account/',include("recruitment.account.urls")),
    url(r'^admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
