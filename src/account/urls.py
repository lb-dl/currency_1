from account import views

from django.urls import path


app_name = 'account'

urlpatterns = [
    # path('my-profile/<int:pk>', views.MyProfile.as_view(), name='my-profile'),
    path('my-profile/', views.MyProfile.as_view(), name='my_profile'),
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('activate/<uuid:username>/', views.ActivateUser.as_view(), name='activate'),
    path('password-change/', views.PasswordChangeView.as_view(), name='password-change'),
    path('avatar/create', views.CreateUserAvatar.as_view(), name='avatar-create'),
    path('avatar/list', views.Avatars.as_view(), name='avatars'),
    path('avatar/<int:pk>', views.delete_avatar, name='avatar-delete'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password-change-done'),
    ]
