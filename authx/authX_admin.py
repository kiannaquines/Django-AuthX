from django.contrib import admin
from .authX_models import AuthXAppUserModel
from django.contrib.auth.admin import UserAdmin as OriginalAdmin
from django.utils.translation import gettext_lazy as _


class AuthXAppUserAdmin(OriginalAdmin):

    list_display = ("id", "username", "email", "date_joined", "last_login")

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


admin.site.register(AuthXAppUserModel, AuthXAppUserAdmin)
