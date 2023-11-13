from django.contrib import admin
from .models import Todo
# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    '''Admin View for Todo'''

    list_display = ('name','created_at')
    list_filter = ('name',)
    search_fields = ('name',)

    ordering = ('name',)