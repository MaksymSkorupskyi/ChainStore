import datetime
from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    GENDER_MALE = True
    GENDER_FEMALE = False
    GENDER_NOT_SURE = None

    GENDER_CHOISES = (
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
        (GENDER_NOT_SURE, _('Not Sure')),
    )

    first_name = models.CharField(max_length=50, verbose_name=_('First Name'))
    last_name = models.CharField(max_length=50, verbose_name=_('Last Name'))
    birthdate = models.DateField(default=datetime.datetime.now, verbose_name=_('birthdate'))
    gender = models.NullBooleanField(choices=GENDER_CHOISES, verbose_name=_('gender'))
    email = models.EmailField(max_length=70, unique=True, verbose_name='e-mail')

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')
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
        return super().get_queryset().filter(gender=Person.GENDER_MALE)


class CustomManagerFemales(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(gender=Person.GENDER_FEMALE)


class MyQuerySet(models.QuerySet):
    def males(self):
        return self.filter(gender=Person.GENDER_MALE)

    def females(self):
        return self.filter(gender=Person.GENDER_FEMALE)

    def name_starts_with(self, s):
        return self.filter(Q(first_name__startswith=s) | Q(last_name__startswith=s))
