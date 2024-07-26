from django.contrib import admin
from .models import AuthXUserModel
from django.contrib.auth.admin import UserAdmin as OriginalAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class AuthXUserAdmin(OriginalAdmin):

    list_display = ("username", "email", "last_login","is_superuser", "is_staff", "is_active",)

    list_display_links = ("username",)
    list_per_page = 25
    search_fields = ("username", "email")
    list_filter = ("date_joined", "last_login")

    fieldsets = (
        (
            _("Login Information"),
            {
                "fields": (
                    "username",
                    "password",
                )
            },
        ),
        (
            _("Personal Information"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone_number_prefix",
                    "phone_number",
                    "user_profile_picture",
                    "birth_date",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Security Features"),
            {
                "fields": (
                    "security_question",
                    "security_question_answer",
                    "failed_login_attempts",
                ),
            },
        ),
        (
            _("Important Dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )

admin.site.register(AuthXUserModel, AuthXUserAdmin)
