from django.urls import path

from .views import ReferralUsersListAPIView


app_name = 'api'

urlpatterns = [
    path('ref_users/', ReferralUsersListAPIView.as_view(), name='ref_users'),
]
