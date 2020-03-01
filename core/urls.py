from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.author.views import AuthorViewSet


router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
