import drf_yasg.openapi
import drf_yasg.views
import rest_framework.permissions


schema_view = drf_yasg.views.get_schema_view(
    drf_yasg.openapi.Info(
        title="PROTester API",
        default_version="v1",
        description="API для сайта PROTester, используемое для отображения данных в реальном времени",
        contact=drf_yasg.openapi.Contact(
            email="dos30028@gmail.com",
            name="Maksim",
        ),
        license=None,
    ),
    public=True,
    permission_classes=(
        rest_framework.permissions.AllowAny,
    ),
)