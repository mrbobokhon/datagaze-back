from django.contrib import admin

from apps.news.models import News


@admin.register(News)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "slug",
        "created_at",
        "active",
    )
    list_display_links = (
        "id",
        "title",
    )
    search_fields = ("title", "sub_title", "text")
    list_filter = ("active", "created_at")
    prepopulated_fields = {"slug": ["title_uz"]}

    fieldsets = (
        ("Основная информация", {"fields": ("cover",)}),
        ("узбекский 🇺🇿", {"fields": ("title_uz", "sub_title_uz", "text_uz", "slug")}),
        ("русский 🇷🇺", {"fields": ("title_ru", "sub_title_ru", "text_ru")}),
        ("английский", {"fields": ("title_en", "sub_title_en", "text_en")}),
    )
