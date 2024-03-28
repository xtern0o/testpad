import rest_framework.response
import rest_framework.status
import rest_framework.viewsets

import api.serializers
import user_tests.models
import users.models


class CategoryViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = user_tests.models.Category.objects.all()
    serializer_class = api.serializers.CategorySerializer


class QuestionImageViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = user_tests.models.QuestionImage.objects.all()
    serializer_class = api.serializers.QuestionImageSerializer


class QuestionViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = user_tests.models.Question.objects.all()
    serializer_class = api.serializers.QuestionSerializer


class QuestionAnswerViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = user_tests.models.QuestionAnswer.objects.all()
    serializer_class = api.serializers.QuestionAnswerSerializer


class TestAvatarViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = user_tests.models.TestAvatar.objects.all()
    serializer_class = api.serializers.TestAvatarSerializer


class TestViewSet(rest_framework.viewsets.ReadOnlyModelViewSet):
    queryset = user_tests.models.Test.objects.all()
    serializer_class = api.serializers.TestSerializer


class UserViewSet(rest_framework.viewsets.ReadOnlyModelViewSet):
    queryset = users.models.CustomUser.objects.all()
    serializer_class = api.serializers.CustomUserDetailSerializer
