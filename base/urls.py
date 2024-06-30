from django.contrib import admin
from django.urls import path, include
from api.models import CourseResource, CategoryResource  # noqa


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('api/', include('api.urls')),
]
