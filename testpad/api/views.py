import rest_framework.response
import rest_framework.status
import rest_framework.viewsets

import api.serializers
import user_tests.managers
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

    def get_queryset(self):
        test_id = self.request.query_params.get("test_id")
        if test_id:
            return user_tests.models.Question.objects.filter_by_test_id(
                test_id,
            )
        return user_tests.models.Question.objects.all()


class QuestionAnswerViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = user_tests.models.QuestionAnswer.objects.all()
    serializer_class = api.serializers.QuestionAnswerSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        test_id = self.request.query_params.get("test_id")
        return user_tests.models.QuestionAnswer.objects.filter_by_tid_or_uid(
            test_id=test_id,
            user_id=user_id,
        )


class TestAvatarViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = user_tests.models.TestAvatar.objects.all()
    serializer_class = api.serializers.TestAvatarSerializer


class TestViewSet(rest_framework.viewsets.ReadOnlyModelViewSet):
    queryset = user_tests.models.Test.objects.all()
    serializer_class = api.serializers.TestSerializer


class UserViewSet(rest_framework.viewsets.ReadOnlyModelViewSet):
    queryset = users.models.CustomUser.objects.all()
    serializer_class = api.serializers.CustomUserDetailSerializer


class TestResultViewSet(rest_framework.viewsets.ModelViewSet):
    queryset = user_tests.models.TestResult.objects.all()
    serializer_class = api.serializers.TestResultSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get("user_id")
        test_id = self.request.query_params.get("test_id")
        return user_tests.models.TestResult.objects.filter_by_tid_or_uid(
            test_id=test_id,
            user_id=user_id,
        )
