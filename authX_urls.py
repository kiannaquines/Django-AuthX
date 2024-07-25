from django.urls import path
from authX.authX_views import AuthXRegisterView, AuthXLoginView,AuthXLogoutView
from authX.authX_settings import AUTHX_SETTINGS

urlpatterns = [
    path(AUTHX_SETTINGS['AUTHX_LOGIN_URL'],AuthXLoginView.as_view(),name="authX_login"),
    path(AUTHX_SETTINGS['AUTHX_REGISTER_URL'],AuthXRegisterView.as_view(),name="authX_register"),
    path(AUTHX_SETTINGS['AUTHX_LOGOUT_URL'],AuthXLogoutView.as_view(),name="authX_logout"),
]