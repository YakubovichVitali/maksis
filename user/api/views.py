from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ReferralUserListSerializer
from ..models import MaksisUser


class ReferralUsersListAPIView(APIView):

    def get(self, request):
        ref_users = MaksisUser.objects.all()
        serializer = ReferralUserListSerializer(ref_users, many=True)
        return Response(serializer.data)
