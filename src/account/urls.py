from account import views

from django.urls import path


app_name = 'account'

urlpatterns = [
    # path('my-profile/<int:pk>', views.MyProfile.as_view(), name='my-profile'),
    path('my-profile/', views.MyProfile.as_view(), name='my_profile'),
    ]
