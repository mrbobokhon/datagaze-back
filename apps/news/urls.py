from django.urls import path

from .views import NewsListView, NewsSingleView, StaticPageListView

urlpatterns = [
    path("all-news/", NewsListView.as_view(), name="news_list"),
    path("single-news/<int:pk>/detail", NewsSingleView.as_view(), name="news_single"),
    path("static-page/", StaticPageListView.as_view(), name="static_page"),
]
