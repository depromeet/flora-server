from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import SocialUserLoginSerializer


class SocialUserLoginAPIView(GenericAPIView):
    # 소셜 유저 로그인
    serializer_class = SocialUserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return Response()