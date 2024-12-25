from django.contrib import admin
from django.urls import path
from django.urls import re_path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from amazon import urls as amazon_urls
from core import urls as core_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r"", include(amazon_urls)),
    re_path(r"", include(core_urls)),
    re_path("^schema/$", SpectacularAPIView.as_view(), name="schema"),
    re_path(
        "^swagger-ui/$",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
