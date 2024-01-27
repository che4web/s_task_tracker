from django.contrib import admin
from taskapp.models import Task,Note

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass
