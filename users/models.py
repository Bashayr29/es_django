from __future__ import unicode_literals

import re

from django.core import validators
from django.db import models


class Users(models.Model):
    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[
            validators.RegexValidator(re.compile('^[a-zA-Z0-9_]+$'), 'Enter a valid username.', 'invalid'),
            validators.MinLengthValidator(limit_value=4)
        ])
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=False, unique=True)