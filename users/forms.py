from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ExtendedUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
                UserCreationForm.Meta.fields
                + ('first_name', 'last_name', 'email')
        )
