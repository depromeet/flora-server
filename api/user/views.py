from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import (
    SocialUserLoginSerializer,
    GuestUstLoginSerializer,
)


class SocialUserLoginAPIView(GenericAPIView):
    # 소셜 유저 로그인
    serializer_class = SocialUserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return Response()


class GuestUserLoginAPIView(APIView):
    # 게스트 유저 로그인
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return Response()