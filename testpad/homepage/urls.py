import django.urls

import homepage.views


app_name = "homepage"

urlpatterns = [
    django.urls.path("", homepage.views.HomepageView.as_view(), name="home"),
]
