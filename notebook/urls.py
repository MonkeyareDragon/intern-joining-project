from django.urls import path
from .views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    ToDoListView,
    NoteGetCreate,
    NoteUpdateDelete
)

urlpatterns = [
    path('', PostListView.as_view(), name='notebook-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='notebook-detail'),
    path('post/new/', PostCreateView.as_view(), name='notebook-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='notebook-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='notebook-delete'),
    path('ToDo', ToDoListView.as_view(), name='todo-list'),
    path('api/note', NoteGetCreate.as_view(), name='api'),
    path('api/note/<int:pk>', NoteUpdateDelete.as_view(), name='update-api'),
]