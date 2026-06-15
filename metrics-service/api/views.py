from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from resources.models import Resource

from .serializers import ResourceSerializer


class ResourceListView(ListAPIView):

    serializer_class = ResourceSerializer

    queryset = (
        Resource.objects
        .filter(is_active=True)
        .order_by("resource_type", "name")
    )