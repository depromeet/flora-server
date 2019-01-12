from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# API 전용 스키마 생성
schema_view = get_schema_view(
   openapi.Info(
      title="Flora API",
      default_version='v1',
      description="Flora API 문서 입니다.",
      terms_of_service="https://naver.com",
      contact=openapi.Contact(email="springkjw@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', 
         include(('api.urls', 'api'), namespace='api')
    ),
    path('admin/', 
         admin.site.urls
    ),

    path('document/', 
        schema_view.with_ui(
            'redoc', 
            cache_timeout=0
        ), name='schema-redoc'
    ),
] + static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
)
