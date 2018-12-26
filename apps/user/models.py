from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager,
)


class UserManager(BaseUserManager):
    # 유저 매니저
    def _create_user(self, *args, **kwargs):
        pass

    def create_superuser(self, *args, **kwargs):
        pass


class User(AbstractBaseUser):
    # 유저 모델
    username = models.CharField(
        '아이디',
        max_legnth=50,
    )
    password = models.CharField(
        '비밀번호',
        max_length=128
    )
    last_login = models.DateTimeField(
        '마지막 로그인',
        blank=True,
    )

    is_admin = models.BooleanField(
        '관리자 여부',
        default=False
    )
    is_active = models.BooleanField(
        '활성화 여부',
        default=False
    )

    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    objects = UserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'users'
        verbose_name = '유저'
        verbose_name_plural = '유저들'

    def __init__(self):
        return self.usernmae

    