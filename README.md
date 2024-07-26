# Django-AuthX
Django-AuthX is a Django library designed to provide a flexible, customizable, easy-to-integrate authentication system for Django applications. 

## Quick start
Download the file in the releases section.
<a href="https://github.com/kiannaquines/Django-AuthX/releases">Django-AuthX Releases</a>

Install the package using `pip`
```
pip install django_authx_system-0.0.1.tar.gz
```

Add `authx` to your `INSTALLED_APPS` list in your Django.
```
INSTALLED_APPS = [..., 'authx',...]
```

Run migrations
```
python manage.py migrate
```

Add the Django-AuthX custom model in the `AUTH_USER_MODEL` in the `settings.py`
```
AUTH_USER_MODEL = 'authx.AuthXUserModel'
```
You can start using
```
python manage.py runserver
```

## Features
* User Registration: Simplified user registration process.
* Login and Logout: Secure and customizable login and logout functionality.
* Templates: Customizable user interfaces (authentication templates)

## Documentation
* To be release
