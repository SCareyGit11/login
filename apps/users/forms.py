from django.forms import ModelForm, PasswordInput
from .models import User

# Create the form class.
class RegisterForm(ModelForm):
     class Meta:
         model = User
         fields = ['first_name', 'last_name', 'email', 'password']
         widgets = {'password':PasswordInput}