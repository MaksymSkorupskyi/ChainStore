from django import forms
from django.core import validators
from decimal import Decimal
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe


# Forms Experiments
class DivErrorList(ErrorList):
    def as_divs(self):
        if not self:
            return ''
        return mark_safe('<div class="errorlist">{}</div>'.format(
            ''.join('<div class="errorlist">{}</div>'.format(e) for e in self)
        ))

    def __str__(self):
        return self.as_divs()


class SendMessageForm(forms.Form):
    name = forms.CharField(
        label='Name',
        min_length=3,
        max_length=50,
        help_text='Enter your name please',
        error_messages={
            'min_length': 'More characters please!',
            'required': 'Please fill input field!',
        },
        show_hidden_initial=True,
        validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(50),
        ],
        localize=True,
    )
    email = forms.EmailField(label='e-mail')
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea({'placeholder': 'Enter your message please'})
    )
    n = forms.DecimalField(
        label='Number',
        localize=True,
        initial=Decimal('1.555'),
        widget=forms.HiddenInput,
    )
