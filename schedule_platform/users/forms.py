from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class RegistrationForm(UserCreationForm):

	class Meta():
		model = User
		fields = ["username", "email", "password1", "password2"]
		labels = {
			"email": "Электронная почта",
			"username": "Логин",
			"password1": "Пароль",
			"password2": "Подтвердить пароль"
		}

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		for name, fields in self.fields.items():
			fields.widget.attrs.update({"class": "form-control"})

class ProfileInfoForm(forms.ModelForm):

	class Meta():
		model = Profile
		fields = ["group", "about"]
		labels = {
			"group": "Группа",
			"about": "Дополнительно"
		}

class LoginForm(forms.Form):
	username = forms.CharField(label="Логин", max_length=100)
	password = forms.CharField(label="Пароль", widget=forms.PasswordInput)