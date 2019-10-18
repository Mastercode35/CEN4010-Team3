"""
Definition of forms.
"""

from django.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = fields.CharField(max_length=254,
                               widget=TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = fields.CharField(label=_("Password"),
                               widget=PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
