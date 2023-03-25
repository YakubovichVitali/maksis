from decimal import Decimal

import mptt

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from mptt.models import (
    MPTTModel,
    TreeForeignKey,
)


class MaksisUser(MPTTModel):

    ref_id = models.CharField(
        unique=True,
        max_length=127,
        verbose_name='Referral id',
    )
    ref_level = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Referral level',
    )
    money_earned = models.DecimalField(
        verbose_name='Money earned',
        decimal_places=2,
        max_digits=8,
        validators=[MinValueValidator(Decimal('0'))],
        null=True,
        blank=True,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Parent',
    )
    owner = models.ManyToManyField(User, related_name='owner', blank=True)

    def __str__(self):
        return f'MaksisUser[{self.pk}] level {self.ref_level}'


mptt.register(MaksisUser)
