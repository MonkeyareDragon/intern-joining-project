from django.contrib import admin
from .models import Note, ToDoTask

# Register your models here.
admin.site.register(Note)
admin.site.register(ToDoTask)