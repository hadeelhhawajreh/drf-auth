from rest_framework import serializers

from .models import Health

class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body')
        model = Health