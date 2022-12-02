from modeltranslation.translator import register, TranslationOptions

from .models import Menu, Slider, Statistic, AboutUs, CompanyCertificate


@register(Menu)
class MenuTranslation(TranslationOptions):
    fields = ("title",)


@register(Slider)
class SliderTranslation(TranslationOptions):
    fields = (
        "title",
        "sub_title",
    )


@register(Statistic)
class StatisticTranslation(TranslationOptions):
    fields = ("title",)


@register(AboutUs)
class AboutUsTranslation(TranslationOptions):
    fields = (
        "title",
        "sub_title",
    )


@register(CompanyCertificate)
class CompanyCertificateTranslation(TranslationOptions):
    fields = (
        "title",
        "sub_title",
        "text",
    )
