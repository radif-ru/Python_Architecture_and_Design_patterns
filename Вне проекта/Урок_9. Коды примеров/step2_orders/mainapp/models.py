from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=16, unique=True, verbose_name='название')


class Phone(models.Model):
    name = models.CharField(max_length=16, unique=True, verbose_name='название модели')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='brand')
    # Возможность иметь пустое поле
    repair_cost = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='цена ремонта', blank=True,
                                      null=True)
    # Новое поле цена продажи
    sale_cost = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='цена продажи', blank=True, null=True)
