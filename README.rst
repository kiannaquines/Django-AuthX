============
Django-authx
============

Django-authx is a Django library designed to provide a flexible, customizable, and easy-to-integrate authentication system for Django applications. 

Django-authx enhances and extends authentication features, allowing developers to efficiently manage user authentication and authorization processes.

Quick start
-----------

Download the package using `pip`

`pip install django-authx`

Add `'authx'` to your `INSTALLED_APPS` list in your Django

`INSTALLED_APPS = [..., 'authx',...]`

Run migrations

`python manage.py migrate`

Start using Django-authx in your Django application.

Features
-----------

* Customizable User Model: Extend or replace Django's default user model with a custom model tailored to your application's needs.

* User Registration: Simplified user registration process with customizable forms and views.

* Login and Logout: Secure and customizable login and logout functionality, with support for various authentication methods.

* Password Management: Built-in support for password reset and change functionality, with customizable email templates and workflows.

* Email Verification: Easy integration of email verification to ensure users confirm their email addresses during registration.

* Session Management: Manage user sessions effectively with built-in support for session expiration and activity tracking.

* Integration with Django Admin: Seamlessly integrates with Django Admin for managing user accounts and permissions.