"""
Definition of forms.
"""

from django import forms as forms1
from django.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms1.CharField(max_length=254,
                               widget=TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms1.CharField(label=_("Password"),
                               widget=PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class ReviewForm (forms1.Form):
    review_message_field=forms1.CharField(label='review_message_field', max_length=300)