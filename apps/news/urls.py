from django.urls import path
from .views import PostListView, PostDetailView, PostFromCategoryView


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', PostFromCategoryView.as_view(), name="post_by_category"),
]