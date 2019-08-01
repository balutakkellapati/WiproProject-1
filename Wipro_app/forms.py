from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Category

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Category
        fields = ('name',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Category
        fields = ('name',)