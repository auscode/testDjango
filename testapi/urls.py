from django.contrib import admin
from django.urls import path,include
from apimovies import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('apimovies/',views.movie_list),
    path('apimovies/<int:id>',views.movie_details),
]

urlpatterns = format_suffix_patterns(urlpatterns)