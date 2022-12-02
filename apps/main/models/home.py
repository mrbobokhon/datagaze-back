from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import OrderModel, ActiveModel


class Menu(OrderModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))

    class Meta:
        db_table = "menu"
        verbose_name = _("Menu ")
        verbose_name_plural = _("1 Menus")
        ordering = ("order",)

    def __str__(self):
        return self.title


class Slider(OrderModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    sub_title = models.CharField(max_length=255, verbose_name=_("sub title"))
    image = models.ImageField(upload_to="slider/image/", verbose_name=_("image"))

    class Meta:
        db_table = "slider"
        verbose_name = _("Slider ")
        verbose_name_plural = _("2 Sliders")
        ordering = ("order",)

    def __str__(self):
        return self.title


class Statistic(OrderModel, ActiveModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    icon = models.ImageField(upload_to="statistic/icon/", verbose_name=_("icon"))

    class Meta:
        db_table = "statistic"
        verbose_name = _("Statistic ")
        verbose_name_plural = _("3 Statistics")
        ordering = ("order",)

    def __str__(self):
        return self.title


class Partner(OrderModel):
    icon = models.ImageField(upload_to="statistic/icon/", verbose_name=_("icon"))
    url = models.URLField(max_length=255, verbose_name=_("Link"))

    class Meta:
        db_table = "partner"
        verbose_name = _("Partner ")
        verbose_name_plural = _("4 Partners")
        ordering = ("order",)
