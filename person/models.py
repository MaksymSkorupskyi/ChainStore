import datetime
from django.db import models
from django.db.models import Q


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
        # get_latest_by = 'birthdate'

    # males = CustomManagerMales()
    # females = CustomManagerFemales()
    # objects = models.Manager()
    # myqs = MyQuerySet.as_manager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def hello_person(self):
        return f'Hello {self}!'


class CustomManagerMales(models.Manager):
    def get_queryset(self):
        return super(CustomManagerMales, self).get_queryset().filter(gender=Person.GENDER_MALE)


class CustomManagerFemales(models.Manager):
    def get_queryset(self):
        return super(CustomManagerFemales, self).get_queryset().filter(gender=Person.GENDER_FEMALE)


class MyQuerySet(models.QuerySet):
    def males(self):
        return self.filter(gender=Person.GENDER_MALE)

    def females(self):
        return self.filter(gender=Person.GENDER_FEMALE)

    def name_starts_with(self, s):
        return self.filter(Q(first_name__startswith=s) | Q(last_name__startswith=s))
