from rest_framework import serializers

from .models import News, StaticPage


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("title", "cover", "slug", "created_at")


class NewsSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("title", "sub_title", "cover", "text", "slug", "created_at")


class StaticPageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticPage
        fields = ("title", "sub_title", "text")
