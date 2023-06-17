from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Note


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
    paginate_by = 5