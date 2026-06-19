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

from metrics.models import MetricData


class MetricDataSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = MetricData

        fields = [
            "timestamp",
            "value",
            "status"
        ]

from rest_framework import serializers


class DashboardSummarySerializer(
    serializers.Serializer
):

    total_resources = serializers.IntegerField()

    green = serializers.IntegerField()

    amber = serializers.IntegerField()

    red = serializers.IntegerField()

class TopOffenderSerializer(
    serializers.Serializer
):

    resource_id = serializers.IntegerField()

    resource_name = serializers.CharField()

    resource_type = serializers.CharField()

    status = serializers.CharField()

class TrendPointSerializer(
    serializers.Serializer
):

    timestamp = serializers.DateTimeField()

    value = serializers.FloatField()

    status = serializers.CharField()


class ResourceHealthSerializer(
    serializers.Serializer
):

    resource_id = serializers.IntegerField()

    resource_name = serializers.CharField()

    resource_type = serializers.CharField()

    status = serializers.CharField()

    last_updated = serializers.DateTimeField()

class AlertSerializer(
    serializers.Serializer
):

    resource_name = serializers.CharField()

    resource_type = serializers.CharField()

    metric_name = serializers.CharField()

    value = serializers.FloatField()

    status = serializers.CharField()

    timestamp = serializers.DateTimeField()

from django.contrib.auth.models import User


class UserSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = User

        fields = [
            "id",
            "username",
            "email"
        ]