from rest_framework import serializers

from resources.models import Resource

from django.contrib.auth.models import User, Group
from metrics.models import MetricDefinition
class ResourceSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField()

    last_updated = serializers.SerializerMethodField()

    metrics_count = serializers.SerializerMethodField()

    class Meta:

        model = Resource

        fields = [
            "id",
            "name",
            "resource_type",
            "environment",
            "is_active",
            "status",
            "last_updated",
            "metrics_count",
        ]
    def get_status(self, obj):

        latest = (
        MetricData.objects
        .filter(resource=obj)
        .order_by("-timestamp")
        .first()
    )

        if latest:
         return latest.status

        return "UNKNOWN"
    
    def get_last_updated(self, obj):

     latest = (
        MetricData.objects
        .filter(resource=obj)
        .order_by("-timestamp")
        .first()
    )

     if latest:
            return latest.timestamp
     return None
    
    def get_metrics_count(self, obj):

        return MetricData.objects.filter(
        resource=obj
        ).count()

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

from rest_framework import serializers


class UserSerializer(
    serializers.ModelSerializer
):

    role = serializers.SerializerMethodField()

    class Meta:

        model = User

        fields = [
            "id",
            "username",
            "email",
            "role"
        ]

    def get_role(self, obj):

        group = obj.groups.first()

        if group:
            return group.name

        return None
    
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    role = serializers.SerializerMethodField()

    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "email",
            "is_active",
            "role"
        ]

    def get_role(self, obj):
        group = obj.groups.first()
        return group.name if group else None
    
class CreateUserSerializer(serializers.ModelSerializer):

    role = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:

        model = User

        fields = [
            "username",
            "email",
            "password",
            "role"
        ]

    def create(self, validated_data):

        role = validated_data.pop("role")
        password = validated_data.pop("password")

        user = User(
            username=validated_data["username"],
            email=validated_data["email"]
        )

        user.set_password(password)
        user.save()

        group = Group.objects.get(name=role)
        user.groups.add(group)

        return user