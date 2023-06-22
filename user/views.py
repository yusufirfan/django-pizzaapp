from django.contrib.auth.views import LoginView, LogoutView

class UserLoginView(LoginView):
    template_name = 'user/user_form.html'
    next_page = 'user_login'

class UserLogoutView(LogoutView):
    template_name = 'user/user_form.html'
    next_page = 'user_login'