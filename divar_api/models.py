from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class Seller (AbstractUser):
    phone_number = models.CharField(blank=True, null=True, max_length=15, verbose_name="موبایل")
    verified = models.BooleanField(default=False, verbose_name="تایید هویت")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'فروشنده'
        verbose_name_plural = ' فروشندگان'


class HouseSpecifications (models.Model):
    name = models.CharField(blank=True, null=True, max_length=256, verbose_name="نام")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ویژگی'
        verbose_name_plural = 'ویژگی ها'


class House (models.Model):
    title = models.CharField(blank=False, null=False, max_length=256, verbose_name="عبارت")
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name="فروشنده", blank=False, null=False, related_name="houses")
    agency = models.CharField(blank=True, null=True, max_length=256, verbose_name="آژانس")
    total_price = models.DecimalField(decimal_places=0, max_digits=18, verbose_name="مبلغ کل")
    price_per_meter = models.DecimalField(decimal_places=0, max_digits=15, verbose_name="مبلغ هر متر")
    floor = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="طبقه")
    specifications = models.ManyToManyField(HouseSpecifications, blank=True)
    city = models.CharField(blank=False, null=False, max_length=256, verbose_name="شهر")
    address = models.TextField(blank=False, null=False, verbose_name="آدرس")
    description = models.TextField(blank=False, null=False, verbose_name="توضیحات")
    datetime_added = models.DateTimeField(auto_now_add=True)
    datetime_last_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'مسکن'
        verbose_name_plural = 'مسکن'
