from django.db import models

from utils.model import DateTimeModel
from apps.user.models import User


def trip_image_path(instance, filename):
    return '{}/{}'.format(
        instance.post.pk,
        filename
    )


class Trip(DateTimeModel):
    # 여행 모델
    name = models.CharField(
        '제목',
        max_length=100
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='유저'
    )
    image = models.ImageField(
        '대표 이미지',
        upload_to=trip_image_path
    )

    class Meta:
        db_table = 'trip'
        verbose_name = '여행'
        verbose_name_plural = '여행들'
        

    def __str__(self):
        return self.name
