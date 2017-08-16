from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    #birth_date and university fields need to be declared seperately because they are not apart of User:
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    university = forms.CharField()

    ROLE = (
        ('CUSTOMER', 'User'),  # (value to be set on model, human readable value)
        ('WORKER', 'Worker'),
    )

    role = forms.ChoiceField(choices=ROLE, required = True)


    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'birth_date','university', 'role', 'password1', 'password2', )