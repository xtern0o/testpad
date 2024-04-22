import django.urls
import rest_framework.routers

import api.swagger
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
router.register(
    "users",
    api.views.UserViewSet,
    basename="users",
)


urlpatterns = [
    django.urls.path(
        "swagger/",
        api.swagger.schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

urlpatterns.extend(router.urls)
