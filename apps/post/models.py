from django.db import models

from utils.model import DateTimeModel
from apps.user.models import User
from apps.trip.models import Trip


class Post(DateTimeModel):
    # 포스트 모델
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='유저'
    )
    trip = models.ForeignKey(
        Trip,
        on_delete=models.CASCADE,
        verbose_name='여행'
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

    class Meta:
        db_table = 'posts'
        verbose_name = '포스트'
        verbose_name_plural = '포스트들'

    def __str__(self):
        return self.title


def post_image_path(instance, filename):
    return '{}/{}'.format(
        instance.post.pk,
        filename
    )

class PostImage(DateTimeModel):
    # 포스트 이미지 모델
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='포스트'
    )
    image = models.ImageField(
        '이미지',
        upload_to=post_image_path
    )
    order = models.SmallIntegerField(
        '순위',
        default=0,
        help_text='숫자가 작을수록 우선순위'
    )

    class Meta:
        db_table = 'post_images'
        verbose_name = '포스트 이미지'
        verbose_name_plural = '포스트 이미지들'
        ordering = ['order']

    def __str__(self):
        return self.post.title
