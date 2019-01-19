from django.db import models

from apps.user.models import User


class Post(models.Model):
    # 글 모델
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='유저'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    title = models.CharField(
        '제목',
        max_length=6
    )
    content = models.CharField(
        '본문',
        max_length=30,
        help_text="최대 30자 입력 가능"
    )
    image = models.ImageField(
        upload_to='images', 
    )

    class Meta:
        db_table = 'post'
        verbose_name = '글'
        verbose_name_plural = '글들'

    def __str__(self):
        return self.name
