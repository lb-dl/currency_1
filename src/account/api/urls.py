from rest_framework.routers import DefaultRouter

from . import views

# app_name = 'api-account'

router = DefaultRouter()
router.register('users', views.UserAPIViewSet, basename='user')
router.register('avatars', views.AvatarAPIViewSet, basename='avatar')

urlpatterns = router.urls
