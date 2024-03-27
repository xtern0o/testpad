import rest_framework.serializers

import users.models


class CustomUserSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = users.models.CustomUser
        fields = [
            "id",
            "username",
            "gender",
            "birthday",
            "image",
            "first_name",
            "middle_name",
            "last_name",
        ]
