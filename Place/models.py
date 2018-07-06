from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ('name',)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.country})'


"""
on_delete now used as the second positional argument 
(previously it was typically only passed as a keyword argument). 
It is be a required argument in Django 2.0.

This is the behaviour to adopt when the referenced object is deleted. 
It is not specific to django, this is an SQL standard.

There are 6 possible actions to take when such event occurs:

CASCADE: 
When the referenced object is deleted, also delete the objects that have references to it 
(When you remove a blog post for instance, you might want to delete comments as well). 
SQL equivalent: CASCADE.

PROTECT: 
Forbid the deletion of the referenced object. 
To delete it you will have to delete all objects that reference it manually. 
Prevent deletion of the referenced object by raising ProtectedError, a subclass of django.db.IntegrityError.
SQL equivalent: RESTRICT.

SET_NULL: 
Set the reference to NULL (requires the field to be nullable). 
For instance, when you delete a User, you might want to keep the comments he posted on blog posts, 
but say it was posted by an anonymous (or deleted) user. 
SQL equivalent: SET NULL.

SET_DEFAULT: 
Set the default value. 
SQL equivalent: SET DEFAULT.

SET(...): 
Set a given value. This one is not part of the SQL standard and is entirely handled by Django.

DO_NOTHING: 
Probably a very bad idea since this would create integrity issues in your database 
(referencing an object that actually doesn't exist). 
SQL equivalent: NO ACTION.

In most cases, CASCADE is the expected behaviour, but for every ForeignKey, 
you should always ask yourself what is the expected behaviour in this situation. 
PROTECT and SET_NULL are often useful. 
Setting CASCADE where it should not, can potentially delete all your database in cascade, 
by simply deleting a single user.

Source: Django documentation
https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ForeignKey.on_delete

See also the documentation of PostGreSQL for instance.
https://www.postgresql.org/docs/current/static/sql-createtable.html
"""
