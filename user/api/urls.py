from django.urls import path

from .views import (
    ReferralUsersListAPIView,
    ReferralUserDetailApiView,
)

app_name = 'api'

urlpatterns = [
    path('ref_users/', ReferralUsersListAPIView.as_view(), name='ref_users'),
    path('ref_user/<str:ref_id>/', ReferralUserDetailApiView.as_view(), name='ref_user_details')
]
