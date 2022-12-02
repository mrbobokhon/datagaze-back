from rest_framework import generics

from apps.main.models import Menu, Slider, Statistic, Partner
from apps.main.serializers.home import (
    MenuListSerializer,
    SliderListSerializer,
    StatisticListSerializer,
    PartnerListSerializer,
)


class MenuListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuListSerializer


class SliderListView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderListSerializer


class StatisticListView(generics.ListAPIView):
    queryset = Statistic.objects.filter(active=True)
    serializer_class = StatisticListSerializer


class PartnerListView(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerListSerializer
