import rest_framework.serializers

import user_tests.models
import users.models


class CustomUserDetailSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = users.models.CustomUser
        exclude = [
            "password",
        ]


class CustomUserShortSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = users.models.CustomUser
        fields = [
            "username",
            "first_name",
            "middle_name",
            "last_name",
            "email",
            "image",
            "last_login",
        ]


class CategorySerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = user_tests.models.Category
        fields = "__all__"


class QuestionImageShortSerializer(
    rest_framework.serializers.ModelSerializer,
):
    class Meta:
        model = user_tests.models.QuestionImage
        fields = [
            user_tests.models.QuestionImage.image.field.name,
        ]


class TestAvatarShortSerializer(
    rest_framework.serializers.ModelSerializer,
):
    class Meta:
        model = user_tests.models.TestAvatar
        fields = [
            user_tests.models.TestAvatar.image.field.name,
        ]


class QuestionImageSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = user_tests.models.QuestionImage
        fields = "__all__"


class QuestionAnswerSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = user_tests.models.QuestionAnswer
        fields = "__all__"


class TestAvatarSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = user_tests.models.TestAvatar
        fields = "__all__"


class QuestionSerializer(rest_framework.serializers.ModelSerializer):
    image = QuestionImageShortSerializer()

    class Meta:
        model = user_tests.models.Question
        fields = "__all__"


class TestSerializer(rest_framework.serializers.ModelSerializer):
    image = TestAvatarShortSerializer()
    questions = QuestionSerializer(many=True, read_only=True)
    author = CustomUserShortSerializer(read_only=True)
    category = rest_framework.serializers.StringRelatedField(read_only=True)

    class Meta:
        model = user_tests.models.Test
        fields = "__all__"


class TestResultSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = user_tests.models.TestResult
        fields = "__all__"
