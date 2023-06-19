from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    title = models.title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=(
        ('Important', 'Important'),
        ('Least Important', 'Least Important')
    ))
    posted_date = models.DateTimeField(default=timezone.now)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.poster.get_username()
    
    def get_absolute_url(self):
        return reverse('notebook-detail', kwargs={'pk': self.pk})

class ToDoTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.note.title} - {self.user.username}"