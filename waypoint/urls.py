from django.contrib import admin
from django.urls import path
from .views import home, report, search, catalog, trail_catalog

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("report/", report, name="report"),
    path("search/", search, name="search"),
    path("catalog/", catalog, name="catalog"),
    path("trails/", trail_catalog, name="trail_catalog"),
]