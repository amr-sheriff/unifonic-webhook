from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

class HomePage(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'home.html'


class Login(LoginView):
    template_name = 'login.html'
