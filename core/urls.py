from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from apps.author.views import AuthorViewSet
from apps.book.views import BookViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Work at Olist Library Project",
      default_version='v1',
      description="",
      contact=openapi.Contact(email="mayron.ceccon@gmail.com"),
      license=openapi.License(name="MIT"),
   ),
   public=True
)

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='authors')
router.register(r'books', BookViewSet, basename='books')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    url(
        r'^documentation(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    url(
        r'^documentation/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
]
