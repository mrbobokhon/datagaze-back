from rest_framework import generics
from rest_framework.views import APIView, Response

from .models import News, StaticPage
from .serializers import NewsListSerializer, NewsSingleSerializer, StaticPageListSerializer


class NewsListView(generics.ListAPIView):
    queryset = News.objects.filter(active=True)
    serializer_class = NewsListSerializer


class NewsSingleView(generics.RetrieveAPIView):
    queryset = News
    serializer_class = NewsSingleSerializer


class StaticPageListView(APIView):
    def get(self, obj, *args, **kwargs):
        queryset = StaticPage.objects.filter(active=True).first()
        serializer = StaticPageListSerializer(queryset, context={"request": self.request})
        return Response(serializer.data)
