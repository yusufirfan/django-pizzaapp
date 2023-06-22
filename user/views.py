from django.contrib.auth.views import LoginView, LogoutView

class FixView:
    template_name = 'user/user_form.html'
    next_page = 'user_login'

class UserLoginView(FixView, LoginView):
    pass

class UserLogoutView(FixView, LogoutView):
    pass

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

class UserCreateView(FixView, CreateView):
    form_class = UserCreationForm
    success_url = '/user/login/'