from datetime import date

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

from avito.settings import MIN_USER_AGE


def check_age(value: date):
    age = relativedelta(date.today(), value).years
    if age < MIN_USER_AGE:
        raise ValidationError(f'Your age ({age}) is too small')


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.name


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Админ"),
    ]

    role = models.CharField(max_length=10, choices=ROLES, default="member")
    age = models.PositiveIntegerField(null=True)
    locations = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[check_age], null=True)
    email = models.EmailField(unique=True, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
