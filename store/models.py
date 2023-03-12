from django.db import models
from django.db.models import PositiveSmallIntegerField


class DateModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)


class Contact(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    email = models.EmailField(null=True, blank=True, unique=True)
    country = models.CharField(max_length=50, null=True, blank=True, verbose_name='Страна')
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name='Город')
    street = models.CharField(max_length=50, null=True, blank=True, verbose_name='Улица')
    house_number = models.CharField(max_length=10, null=True, blank=True, verbose_name='Номер дома')

    def __str__(self):
        return f'{self.country}, {self.city}, {self.street}, {self.house_number}'


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    title = models.CharField(max_length=255, verbose_name='Название')
    model = models.CharField(max_length=255, null=True, blank=True, verbose_name='Модель')
    release_date = models.DateField(null=True, blank=True, verbose_name='Дата производства')

    def __str__(self):
        return self.title


class Supplier(models.Model):
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    class SupType(models.IntegerChoices):
        factory = 0, 'Склад'
        reseller = 1, 'ИП'
        retailer = 2, 'Розничная сеть'

    title = models.CharField(verbose_name='Название', max_length=64)
    type = PositiveSmallIntegerField(
        verbose_name='Тип поставщика', choices=SupType.choices, default=SupType.factory
    )

    def __str__(self):
        return self.title


class Retail(DateModel):
    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'

    title = models.CharField(max_length=255, unique=True, verbose_name='Название')
    contact = models.ForeignKey(
        Contact, on_delete=models.PROTECT, related_name='links', null=True, blank=True, verbose_name='Контакты'
    )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='retailers', null=True, blank=True, verbose_name='Продукт'
    )
    supplier = models.ForeignKey(
        Supplier, on_delete=models.PROTECT, related_name='distributors', null=True, blank=True, verbose_name='Поставщик'
    )
    debt = models.DecimalField(max_digits=11, decimal_places=2, default=0, verbose_name='Задолженность, RUB')

    def __str__(self):
        return self.title