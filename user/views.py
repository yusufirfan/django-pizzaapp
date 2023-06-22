from django.contrib.auth.views import LoginView, LogoutView

REDIRECT_URL = 'user_login'

class FixView:
    template_name = 'user/user_form.html'
    next_page = REDIRECT_URL

class UserLoginView(FixView, LoginView):
    pass

class UserLogoutView(FixView, LogoutView):
    pass

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

class UserCreateView(FixView, CreateView):
    form_class = UserCreationForm
    # success_url = '/user/login/'
    success_url = REDIRECT_URL

    def get_success_url(self):
        from django.contrib.auth import login
        login(self.request, self.object)
        return super().get_success_url()