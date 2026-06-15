from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from resources.models import Resource

from metrics.models import MetricDefinition

from .serializers import (
    ResourceSerializer,
    MetricDefinitionSerializer
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