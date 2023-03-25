from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    ReferralUserListSerializer,
    ReferralUserDetailSerializer,
)
from ..models import MaksisUser


class ReferralUsersListAPIView(APIView):

    def get(self, request):
        ref_users = MaksisUser.objects.all()
        serializer = ReferralUserListSerializer(ref_users, many=True)
        return Response(serializer.data)


class ReferralUserDetailApiView(APIView):

    def get(self, request, ref_id: str):
        ref_user = get_object_or_404(MaksisUser, ref_id=ref_id)
        return Response(ReferralUserDetailSerializer(ref_user).data)
