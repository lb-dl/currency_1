from django.urls import path

from rate import views


app_name = 'rate'

urlpatterns = [
    path('list/', views.RateListView.as_view(), name='list'),
    path('contact-us/create/', views.CreateContactUsView.as_view(), name='contact-us-create'),
    path('feedback/create/', views.CreateFeedbackView.as_view(), name='feedback-create'),
    path('list/csv/', views.CSVView.as_view(), name='list-csv'),
    path('list/xlsx/', views.XLSXView.as_view(), name='list-xlsx'),
    path('list/latest', views.LatestRates.as_view(), name='list-latest'),
    path('update-rate/<int:pk>', views.UpdateRate.as_view(), name='update-rate'),
    path('delete-rate/<int:pk>', views.DeleteRate.as_view(), name='delete-rate'),

    ]
