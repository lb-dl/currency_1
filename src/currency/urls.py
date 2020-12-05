from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

API_PREFIX = 'api/v1'

handler404 = 'rate.views.handler404'
handler500 = 'rate.views.handler500'

urlpatterns = [
    path('account/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('account/', include('account.urls')),
    path('rate/', include('rate.urls')),
    # API
    path(f'{API_PREFIX}/rates/', include('rate.api.urls')),
    path(f'{API_PREFIX}/users/', include('account.api.urls')),
    path(f'{API_PREFIX}/avatars/', include('account.api.urls')),

    path(f'{API_PREFIX}/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_PREFIX}/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    re_path(rf'^{API_PREFIX}/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(rf'^{API_PREFIX}/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(rf'^{API_PREFIX}/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
