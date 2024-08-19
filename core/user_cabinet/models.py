from abc import ABC, abstractmethod

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password,**extra_fields):
        if not email:
            username = extra_fields.get('username')
            email = username
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    REQUIRED_FIELDS = []
    objects = UserManager()
    USERNAME_FIELD = 'email'
    email = models.EmailField(
        _('email addres'),
        unique=True,
        blank=True,
        null=True
    )
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=200,
        help_text=_('Required. 200 characters or fewer.\
                     Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _('A user with that username already exists.'),
        },
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts. '
        ),
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Список пользователей'
        ordering = ('email',)


class Configurations(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
        )


class Plugins(models.Model):
    configuration = models.ManyToManyField(
        Configurations,
        )
    image = models.URLField()
    display_url = models.URLField()
    class Meta:
        abstract = True


class DonationBar(Plugins):
    description = models.CharField(max_length=500,)
    current_value = models.IntegerField()
    target_value = models.IntegerField()
    pass


class MessageAlert(Plugins):
    sender_name = models.CharField(max_length=100)
    sound = models.URLField()
    message = models.TextField()


