from django.contrib import admin
from django.urls import path

from simpleBlog.blog.feeds import LatestPostsFeed
from .views import PostListView, DetailPostView, SharePostView

app_name = "blog"


urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<int:post_id>/share'", SharePostView.as_view(), name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:slug>/",
         DetailPostView.as_view(), name="post_detail"),
    # path("tag/<slug:tag_slug>", PostListView.as_view(), name="post_list_by_tag")
    path("feed/", LatestPostsFeed(), name="post_feed")
]
