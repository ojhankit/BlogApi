from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from .models import CustomUser

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_picture', 'bio', 'phone_number']
