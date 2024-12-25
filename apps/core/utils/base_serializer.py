from django.db import models
from django.utils import timezone

from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    """Base serializer"""

    class Meta:
        abstract = True
    
    def perform_create(self, validated_data, model: models.Model):
        model.objects.update_or_create(
            asin=validated_data["asin"],
            marketplace=validated_data["marketplace"],
            updated_on__date=timezone.now().date(),
            defaults={**validated_data},
        )
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["marketplace"] = instance["marketplace"].name
        return data
