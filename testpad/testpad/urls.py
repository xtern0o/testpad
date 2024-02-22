import django.contrib
import django.urls

urlpatterns = [
    django.urls.path("admin/", django.contrib.admin.site.urls),
    django.urls.path(
        "",
        django.urls.include("homepage.urls"),
    ),
]
