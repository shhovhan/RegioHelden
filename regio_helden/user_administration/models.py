from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.


class AdminUser(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'admin_user'


class CustomUser(models.Model):
    first_name = models.CharField(max_length=50,
                                  validators=[RegexValidator(
                                      r'^[a-zA-Z]+$',
                                      'Enter a valid first name. This value may contain only '
                                      'letters.')]
                                  )
    last_name = models.CharField(max_length=50,
                                 validators=[RegexValidator(
                                     r'^[a-zA-z]+$',
                                     'Enter a valid last name. This value may contain only '
                                     'letters.')]
                                 )
    iban = models.CharField(max_length=50, unique=True,
                            validators=[RegexValidator(
                                r'^[\w]+$',
                                'Enter a valid iban. This value may contain only'
                                'letters, numbers.')]
                            )

    class Meta:
        db_table = 'custom_user'
