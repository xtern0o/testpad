import django.shortcuts
import rest_framework.viewsets
import rest_framework.response
import rest_framework.status

import user_tests.models
import user_tests.serializers


class CategoryViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = user_tests.models.Category.objects.all()
    serializer_class = user_tests.serializers.CategorySerializer


class QuestionImageViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = user_tests.models.QuestionImage.objects.all()
    serializer_class = user_tests.serializers.QuestionImageSerializer


class QuestionViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = user_tests.models.Question.objects.all()
    serializer_class = user_tests.serializers.QuestionSerializer


class QuestionAnswerViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = user_tests.models.QuestionAnswer.objects.all()
    serializer_class = user_tests.serializers.QuestionImageSerializer


class TestAvatarViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = user_tests.models.Avatar.objects.all()
    serializer_class = user_tests.serializers.TestAvatarSerializer


class TestViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = user_tests.models.Test.objects.all()
    serializer_class = user_tests.serializers.TestSerializer
