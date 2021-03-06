from django.contrib import admin
from .models import Todo, Account

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(Todo, TodoAdmin)
admin.site.register(Account)