from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Submit, Div
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
        fields = (
            'name',
            'email',
            'github_username',
            'twitter_username',
            'project',
        )
        model = Attendee

    helper = FormHelper()
    helper.form_method = 'post'
    helper.layout = Layout(
        Div(
            Div(
                Field('name', placeholder='Name*'),
                Field('email', placeholder='Email address*'),
                Field(
                    'github_username',
                    placeholder='Your GitHub username',
                    label='GitHub username (Optional)',
                    ),
                Field(
                    'twitter_username',
                    placeholder='Your Twitter username (without the @)',
                    label='Twitter username (Optional)',
                    ),
                Submit('submit', _('Sign Up!'), css_class='submit'),
                css_class='pull-left form-elements-left',
            ),
            Div(
                Field(
                    'project',
                    rows='5',
                    placeholder='What would you like to work on?',
                    label='What would you like to work on?',
                    ),
                css_class='pull-right form-elements-right',
            ),
            css_class='signup-form',
        )
    )
