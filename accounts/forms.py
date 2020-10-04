from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User This not best praciket
from django.contrib.auth import get_user_model
User = get_user_model()
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.CharField(max_length=254, help_text='Required. Inform avalid email address.' )
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')