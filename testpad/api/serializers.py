import rest_framework.serializers

import user_tests.models
import users.serializers


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
        model = user_tests.models.Avatar
        fields = [
            user_tests.models.Avatar.image.field.name,
        ]


class QuestionImageSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = user_tests.models.QuestionImage
        fields = "__all__"


class QuestionSerializer(rest_framework.serializers.ModelSerializer):
    image = QuestionImageShortSerializer()

    class Meta:
        model = user_tests.models.Question
        fields = "__all__"


class QuestionAnswerSerializer(rest_framework.serializers.ModelSerializer):
    question = QuestionSerializer()
    user = users.serializers.CustomUserSerializer()

    class Meta:
        model = user_tests.models.QuestionAnswer
        fields = "__all__"


class TestAvatarSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = user_tests.models.Avatar
        fields = "__all__"


class TestSerializer(rest_framework.serializers.ModelSerializer):
    image = TestAvatarShortSerializer()
    questions = QuestionSerializer(many=True)
    author = users.serializers.CustomUserSerializer()

    class Meta:
        model = user_tests.models.Test
        fields = "__all__"
