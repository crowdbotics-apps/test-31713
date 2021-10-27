from django.contrib.auth import get_user_model
from rest_framework import serializers
from plans.models import Plan

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"
        read_only_fields = ("created_on", "updated_on")

