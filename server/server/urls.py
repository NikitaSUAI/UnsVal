from django.contrib import admin
from django.urls import path, re_path
from core import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Chatbot API",
        default_version='v1',
        description="Endpoint docs"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # service
    path('admin/', admin.site.urls),
    # api
    path('api/registration/', views.registration, name='registration'),
    path('api/login/', views.log_in, name='login'),
    path('api/answer/', views.get_answer, name='get_answer'),
    # swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
