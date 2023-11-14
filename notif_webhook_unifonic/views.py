from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse

class HomePage(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'home.html'


class Login(LoginView):
    template_name = 'login.html'


def status_view(request):
    return HttpResponse("OK", content_type="text/plain", status=200)
