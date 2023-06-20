from rest_framework import serializers
from notebook.models import Note, ToDoTask

#Create serializers here
class NoteSerializer(serializers.ModelSerializer):
    note_id = serializers.ReadOnlyField()
    class Meta:
        model = Note
        fields = "__all__"