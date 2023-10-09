from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import validate_username
from users.managers import CustomUserManager


class User(AbstractUser):
    """Модель пользователей"""
    # username = models.CharField(
    #     verbose_name='Имя пользователя',
    #     validators=(validate_username,),
    #     max_length=150,
    #     unique=True,
    #     blank=False,
    #     null=False
    # )
    username = None
    email = models.EmailField(
        verbose_name='Email',
        max_length=254,
        unique=True,
        blank=False,
        null=False
    )
    password = models.CharField(
        verbose_name='Пароль',
        max_length=150,
        blank=False,
        null=False
    )

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=False,
        null=False
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=False,
        null=False
    )
    job_title = models.CharField(
        verbose_name='Должность',
        max_length=150,
        blank=False,
        null=False
    )

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'
