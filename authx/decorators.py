from .settings import AUTHX_SETTINGS
from django.shortcuts import redirect

def already_logged_in(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect(AUTHX_SETTINGS['AUTHX_LOGIN_NAME'])
    
    return wrapper_func