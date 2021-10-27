from django.contrib.auth import get_user_model
from rest_framework import serializers
from subscriptions.models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subscription
        fields = "__all__"
        read_only_fields = ("created_on", "updated_on")

