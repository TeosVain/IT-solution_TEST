from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from cashflow_project.constants import (
    MAX_LENGTH, MAX_DIGITS, MAX_DECIMAL, LEN_CURRENCY
)

User = get_user_model()


class Status(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self) -> str:
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    type = models.ForeignKey(
        Type, on_delete=models.CASCADE, related_name='categories'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategories'
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self) -> str:
        return self.name


class CashFlowRecord(models.Model):
    date = models.DateField(
        default=timezone.now, verbose_name='Дата'
    )
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT, verbose_name='Статус'
    )
    type = models.ForeignKey(
        Type, on_delete=models.PROTECT, verbose_name='Тип'
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name='Категория'
    )
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.PROTECT, verbose_name='Подкатегория'
    )
    amount = models.DecimalField(
        max_digits=MAX_DIGITS, decimal_places=MAX_DECIMAL, verbose_name='Сумма'
    )
    currency = models.CharField(
        max_length=LEN_CURRENCY,
        choices=[('RUB', '₽'), ('USD', '$'), ('EUR', '€')],
        default='RUB', verbose_name='Валюта'
    )
    comment = models.TextField(blank=True, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Запись движения средств'
        verbose_name_plural = 'Записи движения средств'

    def __str__(self) -> str:
        return self.comment[:MAX_LENGTH]
