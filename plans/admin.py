from django.contrib import admin
from plans.models import Plan
# Register your models here.

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "desc", "created_at", "updated_at"]