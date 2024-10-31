from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions



# Configs for API Documentation
schema_view = get_schema_view(
    openapi.Info(
        title="API DOCUMENTATION",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [

    # API Documentation Endpoints
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # Admin Panel Endpoint
    path('admin/', admin.site.urls),

    # API Apps Enpoints
    path('api/v1/auth/', include('djoser.urls')),               
    path('api/v1/auth/', include('users.urls')),
]
