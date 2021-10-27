from django.contrib import admin
from apps.models import App
# Register your models here.

@admin.register(App)
class AppAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "desc", "created_at", "updated_at"]