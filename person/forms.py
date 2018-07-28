from datetime import datetime
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import SelectDateWidget, DateInput

from person.models import Person


# class CalendarWidget(forms.TextInput):
#     class Media:
#         extend = False  # по умолчанию True
#         css = {
#             'all': ('pretty.css',)
#         }
#         js = ('animations.js', 'actions.js')


class PersonForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=forms.SelectDateWidget(years=range(datetime.now().year - 100, datetime.now().year + 1)),
        initial=datetime.now(),
        label=_('Birthdate'),
        # input_formats=('%d.%m.%Y', '%d/%m/%Y', '%d-%m-%Y'),
    )

    class Meta:
        model = Person
        fields = '__all__'

# class Media:
#     css = {
#         'all': ('form.css',)
#     }
#     js = ('form.js',)
