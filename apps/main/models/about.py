from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor_uploader.fields import RichTextUploadingField

from apps.common.models import OrderModel, ActiveModel, BaseModel


class AboutUs(ActiveModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    sub_title = models.TextField(verbose_name=_("text"))

    class Meta:
        db_table = "about_us"
        verbose_name = _("About Us ")
        verbose_name_plural = _("About Us'")

    def __str__(self):
        return self.title


class CompanyCertificate(BaseModel, ActiveModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    sub_title = models.CharField(max_length=255, verbose_name=_("sub_title"))
    text = RichTextUploadingField(verbose_name=_("text"))

    class Meta:
        db_table = "company_certificate"
        verbose_name = _("CompanyCertificate ")
        verbose_name_plural = _("CompanyCertificates")

    def __str__(self):
        return self.title


class Certificate(OrderModel, ActiveModel):
    image = models.ImageField(upload_to="certificate/images/", verbose_name=_("image"))

    class Meta:
        db_table = "certificate"
        verbose_name = _("Certificate ")
        verbose_name_plural = _("Certificates")
        ordering = ("order",)


class SocialMedia(OrderModel):
    icon = models.ImageField(upload_to="social_media/icons/", verbose_name=_("icon"))

    class Meta:
        db_table = "social_media"
        verbose_name = _("SocialMedia ")
        verbose_name_plural = _("SocialMedias")
        ordering = ("order",)


class Contact(OrderModel):
    icon = models.ImageField(upload_to="contact/icons/", verbose_name=_("icon"))
    contact = models.CharField(max_length=255, verbose_name=_("contact"))

    class Meta:
        db_table = "contact"
        verbose_name = _("Contact ")
        verbose_name_plural = _("Contacts")
        ordering = ("order",)
