from django.shortcuts import render
from django.views.generic import FormView
from authX.authX_forms import AuthXLoginUserForm, AuthXRegisterUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from authX.authX_settings import AUTHX_SETTINGS
from authX.authX_mixins import RedirectIfAuthenticatedMixin
from django.urls import reverse_lazy

class AuthXRegisterView(RedirectIfAuthenticatedMixin, FormView):
    template_name = 'authX_templates/register.html'
    form_class = AuthXRegisterUserForm
    success_url = AUTHX_SETTINGS['AUTHX_LOGIN_URL']
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
    
class AuthXLogoutView(LogoutView):
    next_page = reverse_lazy('authX_login')


class AuthXLoginView(RedirectIfAuthenticatedMixin, FormView):
    template_name = 'authX_templates/login.html'
    form_class = AuthXLoginUserForm
    success_url = AUTHX_SETTINGS['AUTHX_DASHBOARD_URL']

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)