from django.utils import timezone
from datetime import timedelta
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Note, ToDoTask
from django.shortcuts import render
from rest_framework import generics
from .serializers import NoteSerializer

def home(request):
    context = {
        'notes': Note.objects.all()
    }
    return render(request, 'notebook/home.html', context)

class PostListView(ListView):
    model = Note
    template_name = 'notebook/home.html'  
    context_object_name = 'notes'
    ordering = ['-posted_date']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.GET.get('ordering')  
        yesterday = timezone.localtime() - timedelta(days=1)

        if ordering == 'new_notes':
            queryset = queryset.order_by('-posted_date')
        elif ordering == 'old_notes':
            queryset = queryset.order_by('posted_date')
        elif ordering == 'yesterday_notes':
            queryset = queryset.filter(posted_date__date=yesterday).order_by('-posted_date')
        elif ordering == 'title_notes':
            queryset = queryset.order_by('title')
        return queryset

class PostDetailView(DetailView):
    model = Note

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'description', 'category']

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'description', 'category']

    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.poster:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.poster:
            return True
        return False
    
class ToDoListView(ListView):
    model = ToDoTask
    template_name = 'notebook/ToDoTask.html'  
    context_object_name = 'tasks'
    ordering = ['user']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter tasks by the currently logged-in user
        queryset = queryset.filter(user=self.request.user)
        return queryset
    
class NoteGetCreate(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer