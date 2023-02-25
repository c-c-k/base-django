from django.contrib.auth import forms as auth_forms
# :note: If using a custom User model, comment/remove the next line:
from django.contrib.auth.models import User

# :note: If using a custom User model, uncomment the next line:
# from .models import User


class UserCreationForm(auth_forms.UserCreationForm):
    class Meta:
        model = User
        fields = (
                auth_forms.UserCreationForm.Meta.fields
                + ('first_name', 'last_name', 'email')
        )
