from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms
from .models import CustomUser


class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'age', 'email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','age','email')