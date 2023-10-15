from django.conf import settings
from django.contrib import admin
from django.urls import path, include 
from drf_yasg import openapi 
from drf_yasg.views import get_schema_view 
from rest_framework import permissions



schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="NERD API Endpoints",
        terms_of_service=" ",
        contact=openapi.Contact(email="api.jpp@gmail.com"),
        licecnse=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("redoc/",schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),

]

admin.site.site_header = "NERD Admins"
admin.site.site_tile = " NERD (nginx elasticsearch redis django docker) API"
admin.site.index_title = "Welcome, NERD Admins"

