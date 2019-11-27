"""
Definition of forms.
"""

from django import forms as forms1
from django.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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


class ShoppingForm(forms1.Form):

    card_number = forms1.IntegerField(label='card_num')
    expiration_date = forms1.DateField(label='ex_date')

    primary_flag = forms1.BooleanField(label='primary')





    city = forms1.CharField(label='city')
    state = forms1.CharField(label='state')
    zip_code = forms1.IntegerField(label='zip')
    street = forms1.CharField(label='street')
    street_secondary = forms1.CharField(label='street2')
    country = forms1.CharField(label='address_type')
    apt = forms1.CharField(label='apt')
    f_name = forms1.CharField(label='f_name')
    l_name = forms1.CharField(label='l_name')
    address_type = forms1.CharField(label = 'address_type')

    sale_total = forms1.CharField(label='TOTAL')









class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
 
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username


 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
 
        return password2
 
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

