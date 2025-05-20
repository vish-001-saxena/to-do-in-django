from django.contrib import admin
from .models import todo

@admin.register(todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'created_at', 'updated_at')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('is_completed',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
