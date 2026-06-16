from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from resources.models import Resource

from metrics.models import MetricDefinition



from .serializers import (
    ResourceSerializer,
    MetricDefinitionSerializer,
    MetricDataSerializer
)

from metrics.models import MetricData

from django.utils.dateparse import (
    parse_datetime
)

class ResourceListView(ListAPIView):

    serializer_class = ResourceSerializer

    queryset = (
        Resource.objects
        .filter(is_active=True)
        .order_by("resource_type", "name")
    )

class ResourceMetricsView(
    ListAPIView
):

    serializer_class = (
        MetricDefinitionSerializer
    )

    def get_queryset(self):

        resource_id = self.kwargs[
            "resource_id"
        ]

        resource = Resource.objects.get(
            id=resource_id
        )

        return (
            MetricDefinition.objects
            .filter(
                resource_type=
                resource.resource_type
            )
            .order_by("name")
        )
    

class MetricDataView(
    ListAPIView
):

    serializer_class = (
        MetricDataSerializer
    )

    def get_queryset(self):

        queryset = (
            MetricData.objects
            .select_related(
                "resource",
                "metric"
            )
        )

        resource_id = (
            self.request.GET.get(
                "resource_id"
            )
        )

        metric_id = (
            self.request.GET.get(
                "metric_id"
            )
        )

        start_time = (
            self.request.GET.get(
                "start_time"
            )
        )

        end_time = (
            self.request.GET.get(
                "end_time"
            )
        )

        if resource_id:

            queryset = queryset.filter(
                resource_id=resource_id
            )

        if metric_id:

            queryset = queryset.filter(
                metric_id=metric_id
            )

        if start_time:

            queryset = queryset.filter(
                timestamp__gte=
                parse_datetime(start_time)
            )

        if end_time:

            queryset = queryset.filter(
                timestamp__lte=
                parse_datetime(end_time)
            )

        return (
            queryset
            .order_by("-timestamp")
            [:1000]
        )