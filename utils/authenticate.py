from apps.user.models import SocialUser


class GoogleBackend:
    # 구글 유저 전용 인증
    def authenticate(self, request, uid=None):
        try:
            return SocialUser.objects.get(
                uid=uid
            )
        except SocialUser.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return SocialUser.objects.filter(
                user__id=user_id
            ).user
        except SocialUser.DoesNotExist:
            return None
