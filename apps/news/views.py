from rest_framework import generics

from .models import News
from .serializers import NewsListSerializer, NewsSingleSerializer


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsSingleView(generics.RetrieveAPIView):
    queryset = News
    serializer_class = NewsSingleSerializer
