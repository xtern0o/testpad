import django.contrib.auth.forms
import django.contrib.auth.models
import django.forms
import django.forms.fields

import users.models


class SignUpForm(django.contrib.auth.forms.UserCreationForm):
    email = django.forms.EmailField(
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[
            users.models.CustomUser.birthday.field.name
        ].widget = django.forms.fields.TextInput(
            {
                "type": "date",
            },
        )

    class Meta:
        model = users.models.CustomUser
        fields = [
            users.models.CustomUser.username.field.name,
            users.models.CustomUser.email.field.name,
            users.models.CustomUser.first_name.field.name,
            users.models.CustomUser.last_name.field.name,
            users.models.CustomUser.middle_name.field.name,
            users.models.CustomUser.gender.field.name,
            users.models.CustomUser.birthday.field.name,
        ]
