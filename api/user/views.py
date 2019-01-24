from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework_jwt.views import obtain_jwt_token

from .serializers import (
    SocialUserLoginSerializer,
)
from utils.authenticate import GoogleBackend

class SocialUserLoginAPIView(GenericAPIView):
    # 소셜 유저 로그인
    serializer_class = SocialUserLoginSerializer
    permission_classes = (IsAuthenticated)

    def post(self, request, *args, **kwargs):
        user = GoogleBackend.authenticate(request)
        if user is not None:
            GoogleBackend.get_user(user)
            return obtain_jwt_token
        return Response(status=status.HTTP_401_UNAUTHORIZED)
