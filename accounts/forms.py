from django.contrib.auth import get_user_model
from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=120)
    email = forms.EmailField(required=False, max_length=120)
    password1 = forms.CharField(required=True, max_length=120)
    password2 = forms.CharField(required=True, max_length=120)
    first_name = forms.CharField(required=False, max_length=120)
    last_name = forms.CharField(required=False, max_length=120)

    def clean(self):
        cleaned_data = super().clean()
        user_model = get_user_model()
        errors = {}
        if 'username' in cleaned_data and user_model.objects.filter(username=cleaned_data['username']).exists():
            errors['username'] = ValidationError("A user with that username already exists")
        if 'password1' in cleaned_data and len(cleaned_data['password1']) < 8:
            errors['password1'] = ValidationError("This password is too short. It must contain at least 8 characters")
        if 'password1' in cleaned_data and 'password2' in cleaned_data and cleaned_data['password1'] != cleaned_data['password2']:
            errors['password2'] = ValidationError("The two password fields didn't match")
        if errors:
            raise ValidationError(errors)
        return cleaned_data


class ProfileEditForm(forms.Form):
    first_name = forms.CharField(required=False, max_length=120)
    last_name = forms.CharField(required=False, max_length=120)
    email = forms.EmailField(required=False, max_length=120)
    password1 = forms.CharField(required=False, max_length=120, widget=forms.PasswordInput())
    password2 = forms.CharField(required=False, max_length=120, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        errors = {}
        if 'password1' in cleaned_data and len(cleaned_data['password1']) < 8 and len(cleaned_data['password1']) != 0:
            errors['password1'] = ValidationError("This password is too short. It must contain at least 8 characters")
        if 'password1' in cleaned_data and 'password2' in cleaned_data and cleaned_data['password1'] != cleaned_data[
            'password2']:
            errors['password2'] = ValidationError("The two password fields didn't match")
        if errors:
            raise ValidationError(errors)
        return cleaned_data
