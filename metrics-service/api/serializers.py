from rest_framework import serializers

from resources.models import Resource


class ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resource

        fields = [
            "id",
            "name",
            "resource_type",
            "environment",
            "is_active"
        ]