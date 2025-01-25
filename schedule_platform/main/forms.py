from django import forms

class VerificationForm(forms.Form):
	code = forms.CharField(label="Код подтверждения", max_length=200)