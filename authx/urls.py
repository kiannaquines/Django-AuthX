from django.urls import path
from .views import AuthXRegisterView, AuthXLoginView,AuthXLogoutView
from .settings import AUTHX_SETTINGS

urlpatterns = [
    path('login/',AuthXLoginView.as_view(),name=AUTHX_SETTINGS['AUTHX_LOGIN_NAME']),
    path('register/',AuthXRegisterView.as_view(),name=AUTHX_SETTINGS['AUTHX_REGISTER_NAME']),
    path('logout/',AuthXLogoutView.as_view(),name=AUTHX_SETTINGS['AUTHX_LOGOUT_NAME']),
]