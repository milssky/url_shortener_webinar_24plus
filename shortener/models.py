from django.conf import settings
from django.db import models


class Url(models.Model):
    full_url = models.URLField(
        verbose_name="Сокращаемая ссылка"
    )
    short_url = models.SlugField(
        unique=True,
        verbose_name="Короткая ссылка"
    )
    nums_of_visits = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество посещений"
    )

    def __str__(self) -> str:
        return f"{self.full_url[:settings.SYMBOLS_CUT]} visited {self.nums_of_visits} times"
