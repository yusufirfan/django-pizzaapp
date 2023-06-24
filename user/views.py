from django.contrib.auth.views import LoginView, LogoutView

REDIRECT_URL = 'home'

class FixView:
    template_name = 'user/user_form.html'
    next_page = REDIRECT_URL

class UserLoginView(FixView, LoginView):
    extra_context = {'title': 'Login'} # Sayfa Başlık
    pass

class UserLogoutView(FixView, LogoutView):
    pass

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy



class UserCreateView(FixView, CreateView):
    extra_context = {'title': 'Register'} # Sayfa Başlık
    form_class = UserCreationForm
    # success_url = '/user/login/'
    success_url = reverse_lazy(REDIRECT_URL)

    def get_success_url(self):
        from django.contrib.auth import login
        login(self.request, self.object)
        return super().get_success_url()