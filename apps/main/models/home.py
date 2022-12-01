from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import OrderModel


class Menu(OrderModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))

    class Meta:
        db_table = "menu"
        verbose_name = _("Menu ")
        verbose_name_plural = _("Menus")
        ordering = ("order",)

    def __str__(self):
        return self.title
