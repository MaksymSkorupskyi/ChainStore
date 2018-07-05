import datetime
from django.db import models


class Person(models.Model):
    GENDER_MALE = True
    GENDER_FEMALE = False
    GENDER_NOT_SURE = None

    GENDER_CHOISES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_NOT_SURE, 'Not Sure')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.NullBooleanField(choices=GENDER_CHOISES)
    birthdate = models.DateField(default=datetime.datetime.now)
    email = models.EmailField(max_length=70, unique=True, verbose_name='e-mail')

    class Meta:
        verbose_name = 'Contact person'
        verbose_name_plural = 'Contact persons'
        ordering = ('first_name', 'last_name')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
