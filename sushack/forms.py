from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Submit
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Attendee, MailingListPerson


class MailingListForm(forms.ModelForm):
    class Meta:
        model = MailingListPerson

    helper = FormHelper()
    helper.form_method = 'post'
    helper.layout = Layout(
        Fieldset('',
            Field('email', placeholder='Email address'),
            Field('name', placeholder='Name'),
            Submit('submit', _('Sign Up!'), css_class='submit'),
        )
    )


class SignUpForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'email', 'github_username', 'extra')
        model = Attendee

    helper = FormHelper()
    helper.form_method = 'post'
    helper.layout = Layout(
        Fieldset('',
            Field('name', placeholder='Name*'),
            Field('email', placeholder='Email address*'),
            Field('github_username', placeholder='GitHub User (Optional)'),
            Field('extra', rows='5', placeholder='Anything else? Dietary requirements etc.'),
            Submit('submit', _('Sign Up!'), css_class='submit'),
        )
    )
