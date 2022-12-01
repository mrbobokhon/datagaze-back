from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel, ActiveModel
from ckeditor_uploader.fields import RichTextUploadingField


class News(BaseModel, ActiveModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    sub_title = models.CharField(max_length=255, verbose_name=_("sub title"))
    cover = models.ImageField(upload_to="news/cover/")
    slug = models.SlugField(max_length=255, verbose_name=_("slug"))
    text = RichTextUploadingField(verbose_name=_("text"))

    class Meta:
        db_table = "news"
        verbose_name = _("News")
        verbose_name_plural = _("News")
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class StaticPage(BaseModel, ActiveModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    sub_title = models.CharField(max_length=255, verbose_name=_("sub title"))
    text = RichTextUploadingField(verbose_name=_("text"))

    class Meta:
        db_table = "static_page"
        verbose_name = _("Static Page ")
        verbose_name_plural = _("Static Pages")
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
