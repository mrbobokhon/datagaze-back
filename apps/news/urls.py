from django.urls import path

from .views import NewsListView, NewsSingleView

urlpatterns = [
    path("all-news/", NewsListView.as_view(), name="news_list"),
    path("single-news/<int:pk>/detail", NewsSingleView.as_view(), name="news_single"),
]
