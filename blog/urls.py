from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostList.as_view(), name="blog"),
    path('add', views.AddPostView.as_view(), name='add'),
    path('<slug:slug>/edit', views.EditPostView.as_view(), name='edit'),
    path('<slug:slug>/delete', views.DeletePostView.as_view(), name='delete'),
    path("<slug:slug>", views.PostDetail.as_view(), name="blog_details"),
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),
]
