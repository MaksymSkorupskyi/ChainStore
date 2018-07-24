from django import forms
from person.models import Person


class CalendarWidget(forms.TextInput):
    class Media:
        css = {
            'all': ('pretty.css',),
        }
        js = ('animation.js', 'action.js')


class PersonForm(forms.ModelForm):
    # test =
    class Meta:
        model = Person
        fields = '__all__'
