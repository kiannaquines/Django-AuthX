from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import datetime

class AuthXAppUserModel(AbstractUser):
    first_name = models.CharField(
        max_length=50,
        unique=False,
        help_text="First name",
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=50,
        unique=False,
        help_text="Last name",
        null=True,
        blank=True,
    )
    username = models.CharField(
        max_length=50,
        unique=True,
        help_text="Username",
        error_messages= {
            "unique": "A user with that username already exists.",
            "required": "This field cannot be blank."
        }
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        help_text="Email address",
        error_messages= {
            "unique": "A user with that email already exists.",
            "required": "This field cannot be blank."
        }
    )
    phone_number_prefix = models.CharField(
        max_length=10,
        unique=False,
        help_text="Phone number prefix (e.g., +1, +63, etc.)",
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        help_text="Phone number (e.g., 09050673466)",
        null=True,
        blank=True,
    )
    failed_login_attempts = models.PositiveIntegerField(
        default=0, help_text="Failed login attempts"
    )
    password_last_updated = models.DateTimeField(
        auto_now=True, help_text="Last password update timestamp"
    )
    security_question = models.CharField(
        max_length=255,
        unique=False,
        help_text="Security question",
        null=True,
        blank=True,
    )
    security_question_answer = models.CharField(
        max_length=255,
        unique=False,
        help_text="Security question answer",
        null=True,
        blank=True,
    )
    user_profile_picture = models.ImageField(
        upload_to="user_profile_pictures/",
        help_text="User profile picture",
        null=True,
        blank=True,
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        help_text="Date of birth",
    )

    class Meta:
        db_table = "auth_user"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.username
    
    def getUserName(self) -> str:
        return self.username
    
    def getFullname(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    def getPhoneNumber(self) -> str:
        return f'{self.phone_number_prefix} {self.phone_number}'
    
    def isBirthday(self) -> bool:
        today = datetime.date.today()
        return today.month == self.birth_date.month and today.day == self.birth_date.day
    
