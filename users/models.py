from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=1024)
    # zip_code = models.CharField(_("zip_code"), maax_length=5, default="43701",
    #                             validators=[RegexValidator(
    #
    #                             )]
    #                             )
    zip_code = models.CharField(max_length=5, default="43701",
        validators=[RegexValidator(
            regex=r'^\d{5}$',
            message='Must be valid zipcode in formats from 00000 to 99999',
        )])
    phone_number = models.CharField(max_length=15, default="000000000",
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
        )])