from rest_framework import serializers

from apps.main.models import Menu, Slider, Statistic, Partner


class MenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ("title",)


class SliderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ("title", "sub_title", "image")


class StatisticListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ("title", "icon")


class PartnerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ("icon", "url")
