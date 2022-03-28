from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostList.as_view(), name="blog"),
    path('post_form', views.PostFormView.as_view(), name='post_form'),
    path("<slug:slug>", views.PostDetail.as_view(), name="blog_details"),
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),
]
