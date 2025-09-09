from django import forms
from .models import LoginModel


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = LoginModel
        fields =  [
            'email',
            'password'
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data