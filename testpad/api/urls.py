import django.urls
import rest_framework.routers

import api.views


app_name = "api"

router = rest_framework.routers.DefaultRouter()
router.register(
    "categories",
    api.views.CategoryViewSet,
    basename="categories",
)
router.register(
    "questions",
    api.views.QuestionViewSet,
    basename="questions",
)
router.register(
    "questions_answers",
    api.views.QuestionAnswerViewSet,
    basename="questions_answers",
)
router.register(
    "tests",
    api.views.TestViewSet,
    basename="tests",
)

urlpatterns = []

urlpatterns.extend(router.urls)
