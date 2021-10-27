from django.contrib.auth import get_user_model
from rest_framework import serializers
from apps.models import App

User = get_user_model()

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = "__all__"
        read_only_fields = ("user", "created_on", "updated_on")

    def create(self, validated_data):
        request = self.context['request']
        
        instance = self.Meta.model._default_manager.create(
            **validated_data,
            **{
                'user': request.user
            }
        )
        return instance
