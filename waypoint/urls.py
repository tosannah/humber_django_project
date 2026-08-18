from django.contrib import admin
from django.urls import path
from .views import home, report, search, catalog, trail_catalog
from trails.views import trails_by_park

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("report/", report, name="report"),
    path("search/", search, name="search"),
    path("catalog/", catalog, name="catalog"),
    path("trails/", trail_catalog, name="trail_catalog"),
    path("trails/park/<int:park_id>/", trails_by_park, name="trails_by_park"),
]