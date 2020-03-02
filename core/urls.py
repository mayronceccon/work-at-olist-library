from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.author.views import AuthorViewSet
from apps.book.views import BookViewSet


router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]
