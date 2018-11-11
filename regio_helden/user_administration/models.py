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
                                      'Enter a valid first name.'
                                      'This value may contain only letters.')]
                                  )
    last_name = models.CharField(max_length=50,
                                 validators=[RegexValidator(
                                     r'^[a-zA-z]+$',
                                     'Enter a valid last name.'
                                     'This value may contain only letters.')]
                                 )
    iban = models.CharField(max_length=34, unique=True,
                            validators=[RegexValidator(
                                r'^[A-Z]{2}[0-9]{2}[a-zA-z0-9]{4}[0-9]{7}([a-zA-z0-9]?){0,19}$',
                                'Enter a valid IBAN. It should start with '
                                'country code and may contain only letters, '
                                'numbers.')]
                            )

    class Meta:
        db_table = 'custom_user'
        permissions = (
            ('edit_user', 'Edit user'),
            ('delete_user', 'Delete user'),
        )

    def __str__(self):
        return '%s %s', (self.first_name, self.last_name)
