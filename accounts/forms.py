from django.contrib.auth import forms as auth_forms

from .models import User


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = (
                auth_forms.UserCreationForm.Meta.fields
                + ('first_name', 'last_name', 'email')
        )
