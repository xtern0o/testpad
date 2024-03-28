import django.conf.urls
import django.conf.urls.static
import django.contrib
import django.urls

urlpatterns = [
    django.urls.path("admin/", django.contrib.admin.site.urls),
    django.urls.path(
        "api/",
        django.urls.include("api.urls"),
    ),
    django.urls.path(
        "tests/",
        django.urls.include("user_tests.urls"),
    ),
    django.urls.path(
        "",
        django.urls.include("homepage.urls"),
    ),
]

urlpatterns += django.conf.urls.static.static(
    django.conf.settings.STATIC_URL,
    document_root=django.conf.settings.STATIC_ROOT,
)
urlpatterns += django.conf.urls.static.static(
    django.conf.settings.MEDIA_URL,
    document_root=django.conf.settings.MEDIA_ROOT,
)

if django.conf.settings.DEBUG:
    import debug_toolbar

    urlpatterns += (
        django.urls.path(
            "__debug__/",
            django.urls.include(debug_toolbar.urls),
        ),
    )
