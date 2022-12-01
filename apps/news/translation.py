from modeltranslation.translator import register, TranslationOptions

from apps.news.models import News, StaticPage


@register(News)
class NewsTranslation(TranslationOptions):
    fields = ("title", "sub_title", "text")


@register(StaticPage)
class StaticPageTranslation(TranslationOptions):
    fields = ("title", "sub_title", "text")
