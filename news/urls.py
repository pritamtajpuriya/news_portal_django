from django.urls.conf import path
from news.views import *


#  URLS for news app
#  Path: news\urls.py


urlpatterns = [
    path("subsription/", subscription, name="subscription"),
    path("category-list/", CategoryList.as_view(), name="category-list"),
    path("category-news/<int:id>/", NewsList.as_view(), name="news-list"),
    path("main-news/", MainNewsList.as_view(), name="main-news"),
    path("recent-update/", RecentUpdateList.as_view(), name="recent-update"),
]
