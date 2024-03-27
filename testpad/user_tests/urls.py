import django.urls
import rest_framework.routers

import user_tests.views


app_name = "user_tests"

router = rest_framework.routers.DefaultRouter()
router.register(
    "api/categories/",
    user_tests.views.CategoryViewSet,
    basename="categories",
)
router.register(
    "api/questions/",
    user_tests.views.QuestionViewSet,
    basename="questions",
)
router.register(
    "api/questions_answers/",
    user_tests.views.QuestionAnswerViewSet,
    basename="questions_answers",
)
router.register(
    "api/tests/",
    user_tests.views.TestViewSet,
    basename="tests",
)

urlpatterns = []

urlpatterns.extend(router.urls)
