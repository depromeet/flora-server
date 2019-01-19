from django.db import models

from utils.model import DateTimeModel
from apps.user.models import User


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

    class Meta:
        db_table = 'trip'
        verbose_name = '여행'
        verbose_name_plural = '여행들'
        

    def __str__(self):
        return self.name
