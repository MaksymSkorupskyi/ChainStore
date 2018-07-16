from django import forms


class SendMessageForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    email = forms.EmailField(label='e-mail')
    message = forms.CharField(label='Message', widget=forms.Textarea({'placeholder': 'Enter your message please'}))
