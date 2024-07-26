# Django-AuthX


Django-AuthX is a Django library designed to provide a flexible, customizable, easy-to-integrate authentication system for Django applications. 
Django-AuthX enhances and extends authentication features, allowing developers to manage user authentication and authorization processes efficiently.

## Quick start
-----------

Download the package using `pip`

```
pip install django-authx
```

Add `authx` to your `INSTALLED_APPS` list in your Django.

```
INSTALLED_APPS = [..., 'authx',...]
```

Run migrations

```
python manage.py migrate
```

Add the Django-AuthX custom model in the `AUTH_USER_MODEL` in the 

You can start using Django-Authx in your Django application settings.py

```
AUTH_USER_MODEL = 'authx.AuthXUserModel'
```

## Features

* User Registration: Simplified user registration process.
* Login and Logout: Secure and customizable login and logout functionality.
