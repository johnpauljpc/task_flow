from rest_framework import serializers
from django.contrib.auth import get_user_model
from datetime import date, timedelta, datetime

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Task
        fields = ['id','title', 'description', 'owner', 'due_date', 'completed', 'priority',
                  "created_on", "updated_on"]
        read_only_fields = ["ownner","created_on", "updated_on"]

    # Ensures a user is logged in before creating task
    def create(self, validated_data):
        user = self.context['request'].user
        if not user.id:
            raise serializers.ValidationError("Login to create task!")
        validated_data['owner'] = user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        user = self.context['request'].user
        if not (user.id == instance.owner.id):
            raise serializers.ValidationError("You are not authorized to update this task!")
        return super().update(instance, validated_data)
