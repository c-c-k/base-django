from django.contrib.auth.forms import UserCreationForm


class UserCreationFormWithPersonalInfo(UserCreationForm):
    class Meta:
        fields = (
                UserCreationForm.Meta.fields
                + ('first_name', 'last_name', 'email')
        )
