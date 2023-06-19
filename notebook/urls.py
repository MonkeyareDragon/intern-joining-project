from django.urls import path
from .views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='notebook-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='notebook-detail'),
    path('post/new/', PostCreateView.as_view(), name='notebook-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='notebook-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='notebook-delete'),
]