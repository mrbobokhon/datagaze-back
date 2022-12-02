from django.contrib import admin

from .models import AboutUs, CompanyCertificate, Certificate, SocialMedia, Contact
from .models.home import Menu, Slider, Statistic, Partner


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
    )
    list_display_links = (
        "id",
        "title",
    )
    search_fields = ("title", "sub_title", "text")

    fieldsets = (
        (
            "Основная информация",
            {"fields": ("order",)},
        ),
        ("узбекский 🇺🇿", {"fields": ("title_uz",)}),
        ("русский 🇷🇺", {"fields": ("title_ru",)}),
        ("английский 🇺🇸", {"fields": ("title_en",)}),
    )


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "sub_title")
    list_display_links = (
        "id",
        "title",
    )
    search_fields = ("title", "sub_title")

    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "image",
                    "order",
                )
            },
        ),
        (
            "узбекский 🇺🇿",
            {
                "fields": (
                    "title_uz",
                    "sub_title_uz",
                )
            },
        ),
        (
            "русский 🇷🇺",
            {
                "fields": (
                    "title_ru",
                    "sub_title_ru",
                )
            },
        ),
        (
            "английский 🇺🇸",
            {
                "fields": (
                    "title_en",
                    "sub_title_en",
                )
            },
        ),
    )


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
    )
    list_display_links = (
        "id",
        "title",
    )
    search_fields = ("title",)
    list_filter = ("active",)
    fieldsets = (
        (
            "Основная информация",
            {"fields": ("icon", "order", "active")},
        ),
        ("узбекский 🇺🇿", {"fields": ("title_uz",)}),
        ("русский 🇷🇺", {"fields": ("title_ru",)}),
        ("английский 🇺🇸", {"fields": ("title_en",)}),
    )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "url",
        "icon",
    )
    list_display_links = (
        "id",
        "url",
    )
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "icon",
                    "url",
                    "order",
                )
            },
        ),
    )


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "sub_title", "active")
    list_display_links = (
        "id",
        "title",
    )
    search_fields = ("title", "sub_title")

    fieldsets = (
        (
            "Основная информация",
            {"fields": ("active",)},
        ),
        (
            "узбекский 🇺🇿",
            {
                "fields": (
                    "title_uz",
                    "sub_title_uz",
                )
            },
        ),
        (
            "русский 🇷🇺",
            {
                "fields": (
                    "title_ru",
                    "sub_title_ru",
                )
            },
        ),
        (
            "английский 🇺🇸",
            {
                "fields": (
                    "title_en",
                    "sub_title_en",
                )
            },
        ),
    )

    def has_add_permission(self, request):
        if AboutUs.objects.filter(active=True).exists():
            return False
        else:
            return True


@admin.register(CompanyCertificate)
class CompanyCertificateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "sub_title",
        "created_at",
        "active",
    )
    list_display_links = (
        "id",
        "title",
    )
    search_fields = ("title", "sub_title", "text")
    list_filter = ("active",)
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "certificate",
                    "active",
                )
            },
        ),
        ("узбекский 🇺🇿", {"fields": ("title_uz", "sub_title_uz", "text_uz")}),
        ("русский 🇷🇺", {"fields": ("title_ru", "sub_title_ru", "text_ru")}),
        ("английский 🇺🇸", {"fields": ("title_en", "sub_title_en", "text_en")}),
    )

    def has_add_permission(self, request):
        if CompanyCertificate.objects.filter(active=True).exists():
            return False
        else:
            return True


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "active")
    list_display_links = (
        "id",
        "image",
    )
    list_filter = ("active",)
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "image",
                    "active",
                    "order",
                )
            },
        ),
    )


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "link",
        "icon",
    )
    list_display_links = (
        "id",
        "link",
    )
    fieldsets = (
        (
            "Основная информация",
            {
                "fields": (
                    "icon",
                    "link",
                    "order",
                )
            },
        ),
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "contact",
        "icon",
    )
    list_display_links = ("id", "contact")
    fieldsets = (
        (
            "Основная информация",
            {"fields": ("icon", "order", "contact")},
        ),
    )
