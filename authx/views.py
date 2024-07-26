from django.views.generic import FormView
from .forms import AuthXLoginForm, AuthXRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from .settings import AUTHX_SETTINGS
from .mixins import RedirectIfAuthenticatedMixin
from django.urls import reverse_lazy

class AuthXRegisterView(RedirectIfAuthenticatedMixin, FormView):
    template_name = 'register.html'
    form_class = AuthXRegisterForm
    success_url = reverse_lazy(AUTHX_SETTINGS['AUTHX_LOGIN_NAME'])
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super().form_valid(form)
    
class AuthXLogoutView(LogoutView):
    next_page = reverse_lazy(AUTHX_SETTINGS['AUTHX_LOGIN_NAME'])


class AuthXLoginView(RedirectIfAuthenticatedMixin, FormView):
    template_name = 'login.html'
    form_class = AuthXLoginForm
    success_url = reverse_lazy(AUTHX_SETTINGS['AUTHX_SUCCESS_NAME'])

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)