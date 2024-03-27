import rest_framework.serializers

import users.serializers
import user_tests.models


class CategorySerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = user_tests.models.Category
        fields = "__all__"


class QuestionImageSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = user_tests.models.QuestionImage
        fields = "__all__"


class QuestionSerializer(rest_framework.serializers.ModelSerializer):
    image = QuestionImageSerializer()

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
    image = TestAvatarSerializer()
    questions = QuestionSerializer(many=True)
    author = users.serializers.CustomUserSerializer()

    class Meta:
        model = user_tests.models.Test
        fields = "__all__"
