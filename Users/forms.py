from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# in order to added extra email fields and to keep the configuration one place
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )
    class Meta:
        model=User
        fields=['username','email','password1']

