from django.urls import path
from .views import PostCreateView, PostListView, PostDetailView

urlpatterns = [
    path('api/posts/', PostListView.as_view(), name='post-list'),
    path('api/posts/create/', PostCreateView.as_view(), name='post-create'),
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
