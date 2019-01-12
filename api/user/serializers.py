from rest_framework import serializers

from apps.user.constants import (
    PROVIDER_TYPE, PROVIDER_GOOGLE
)


class SocialUserLoginSerializer(serializers.Serializer):
    # 소셜 유저 로그인 직렬화
    provider = serializers.ChoiceField(
        label='소셜 플랫폼',
        choices=PROVIDER_TYPE,
        default=PROVIDER_GOOGLE
    )
    code = serializers.CharField(
        label='코드'
    )
    redirect = serializers.CharField(
        label='리다이렉트 주소'
    )

    def authenticate(self):
        pass