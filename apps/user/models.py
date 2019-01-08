from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager,
)
from django.contrib.postgres.fields import JSONField

from .constants import (
    PROVIDER_GOOGLE, PROVIDER_TYPE,
)

class UserManager(BaseUserManager):
    # 유저 매니저
    def _create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError("아이디는 필수입니다.")
        
        user = self.model(
            username=usernname,
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault('is_admin', True)

        return self._create_user(username, password, **kwargs)


class User(AbstractBaseUser):
    # 유저 모델
    username = models.CharField(
        '아이디',
        max_length=50,
        unique=True
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
        default=True
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

    def __str__(self):
        return self.usernmae


class SocialApp(models.Model):
    provider = models.CharField(
        '플랫폼 종류',
        max_length=20,
        choices=PROVIDER_TYPE
    )
    name = models.CharField(
        '이름',
        max_length=30
    )
    client_id = models.CharField(
        '클라이언트 ID',
        max_length=191
    )
    secret = models.CharField(
        '시크릿',
        max_length=191
    )
    key = models.CharField(
        '키',
        max_length=191,
        blank=True
    )

    class Meta:
        db_table = 'social_apps'
        verbose_name = '소셜 앱'
        verbose_name_plural = '소셜 앱들'

    
class SocialUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='유저'
    )
    provider = models.CharField(
        '소셜 플랫폼',
        max_length=20,
        choices=PROVIDER_TYPE,
        default=PROVIDER_GOOGLE
    )
    uid = models.CharField(
        'UID',
        max_length=150
    )
    extra_data = JSONField(
        '기타 정보',
        default=dict
    )

    class Meta:
        db_table = 'social_users'
        verbose_name = '소셜 유저'
        verbose_name_plural = '소셜 유저들'

    def __str__(self):
        return self.user.username
