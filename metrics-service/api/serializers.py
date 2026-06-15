from rest_framework import serializers

from resources.models import Resource


from metrics.models import MetricDefinition
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



class MetricDefinitionSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = MetricDefinition

        fields = [
            "id",
            "name",
            "unit",
            "warning_threshold",
            "critical_threshold"
        ]