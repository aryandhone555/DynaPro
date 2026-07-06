from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from resources.models import Resource

from metrics.models import MetricDefinition

from datetime import timedelta

from django.utils import timezone

from .serializers import (
    ResourceSerializer,
    MetricDefinitionSerializer,
    MetricDataSerializer,
    DashboardSummarySerializer,
    TopOffenderSerializer,
    TrendPointSerializer,
    ResourceHealthSerializer,
    AlertSerializer,
    CreateUserSerializer

)

from django.contrib.auth.models import User
from .permissions import IsAdminRole
from .serializers import UserSerializer

from metrics.models import MetricData
from rest_framework import status
from rest_framework.permissions import IsAuthenticated #JWT AUTHENTICATION

from django.shortcuts import get_object_or_404

from django.utils.dateparse import (
    parse_datetime
)

# from django.db.models import OuterRef
# from django.db.models import Subquery
# from django.db.models import Count

from django.db.models import Max



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
    permission_classes = [IsAuthenticated]

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
    permission_classes = [IsAuthenticated]

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
    
from rest_framework.response import Response
from rest_framework.views import APIView

class DashboardSummaryView(APIView):
    from .permissions import IsAdminRole
    permission_classes = [IsAuthenticated]

    def get(self, request):

        latest_timestamps = (
            MetricData.objects
            .values("resource_id")
            .annotate(
                latest_time=Max("timestamp")
            )
        )

        green = 0
        amber = 0
        red = 0

        for row in latest_timestamps:

            latest_record = (
                MetricData.objects
                .filter(
                    resource_id=row["resource_id"],
                    timestamp=row["latest_time"]
                )
                .first()
            )

            if not latest_record:
                continue

            if latest_record.status == "GREEN":
                green += 1

            elif latest_record.status == "AMBER":
                amber += 1

            elif latest_record.status == "RED":
                red += 1

        data = {

            "total_resources":
            Resource.objects.filter(
                is_active=True
            ).count(),

            "green": green,
            "amber": amber,
            "red": red,
        }

        serializer = DashboardSummarySerializer(
            data
        )

        return Response(
            serializer.data
        )
    

class TopOffendersView(APIView):    
    permission_classes = [IsAuthenticated]

    def get(self, request):

        latest_timestamps = (
            MetricData.objects
            .values("resource_id")
            .annotate(
                latest_time=Max("timestamp")
            )
        )

        offenders = []

        for row in latest_timestamps:

            latest_record = (
                MetricData.objects
                .select_related(
                    "resource"
                )
                .filter(
                    resource_id=row["resource_id"],
                    timestamp=row["latest_time"]
                )
                .first()
            )

            if not latest_record:
                continue

            if latest_record.status in [
                "RED",
                "AMBER"
            ]:

                offenders.append({

                    "resource_id":
                    latest_record.resource.id,

                    "resource_name":
                    latest_record.resource.name,

                    "resource_type":
                    latest_record.resource.resource_type,

                    "status":
                    latest_record.status
                })

        status_order = {
            "RED": 0,
            "AMBER": 1
        }

        offenders.sort(
            key=lambda x:
            status_order[x["status"]]
        )

        serializer = (
            TopOffenderSerializer(
                offenders,
                many=True
            )
        )

        return Response(
            serializer.data
        )
    

class DashboardTrendView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        resource_id = request.GET.get("resource_id")
        metric_id = request.GET.get("metric_id")

        minutes = int(request.GET.get("minutes", 60))

        end_time = timezone.now()
        start_time = end_time - timedelta(minutes=minutes)

        queryset = MetricData.objects.filter(
         timestamp__gte=start_time,
         timestamp__lte=end_time,
         )

    # Optional filtering
        if resource_id:
            queryset = queryset.filter(resource_id=resource_id)

        if metric_id:
            queryset = queryset.filter(metric_id=metric_id)

    # Default dashboard chart:
    # Payment Service + Response Time
        if not resource_id and not metric_id:

             latest = (
              MetricData.objects
             .order_by("-timestamp")
             .first()
                )

             if latest:
                  queryset = queryset.filter(
                  resource=latest.resource,
                     metric=latest.metric
                )

        # if resource and metric:
        #     queryset = queryset.filter(
        #         resource=resource,
        #         metric=metric
        #     )

        queryset = (
        queryset
        .order_by("timestamp")
        .values(
            "timestamp",
            "value",
            "status"
        )
    )

        serializer = TrendPointSerializer(
        queryset,
        many=True
    )

        return Response(serializer.data)


class ResourceHealthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        latest_timestamps = (
            MetricData.objects
            .values("resource_id")
            .annotate(
                latest_time=Max("timestamp")
            )
        )

        results = []

        for row in latest_timestamps:

            latest_record = (
                MetricData.objects
                .select_related(
                    "resource"
                )
                .filter(
                    resource_id=row["resource_id"],
                    timestamp=row["latest_time"]
                )
                .first()
            )

            if not latest_record:
                continue

            results.append({

                "resource_id":
                latest_record.resource.id,

                "resource_name":
                latest_record.resource.name,

                "resource_type":
                latest_record.resource.resource_type,

                "status":
                latest_record.status,

                "last_updated":
                latest_record.timestamp
            })

        serializer = (
            ResourceHealthSerializer(
                results,
                many=True
            )
        )

        return Response(
            serializer.data
        )
class AlertsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):

        latest_records = []

        for resource in Resource.objects.filter(
            is_active=True
        ):

            metrics = MetricDefinition.objects.filter(
                resource_type=resource.resource_type
            )

            for metric in metrics:

                latest_record = (
                    MetricData.objects
                    .select_related(
                        "resource",
                        "metric"
                    )
                    .filter(
                        resource=resource,
                        metric=metric
                    )
                    .order_by(
                        "-timestamp"
                    )
                    .first()
                )

                if (
                    latest_record and
                    latest_record.status != "GREEN"
                ):
                    latest_records.append(
                        latest_record
                    )

        alerts = []

        for record in latest_records:

            alerts.append({

                "resource_name":
                record.resource.name,

                "resource_type":
                record.resource.resource_type,

                "metric_name":
                record.metric.name,

                "value":
                record.value,

                "status":
                record.status,

                "timestamp":
                record.timestamp
            })

        alerts.sort(
            key=lambda x: (
                0 if x["status"] == "RED"
                else 1
            )
        )

        serializer = AlertSerializer(
            alerts,
            many=True
        )

        return Response(
            serializer.data
        )
    
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
class CurrentUserView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        serializer = UserSerializer(
            request.user
        )

        return Response(
            serializer.data
        )
    
class UserListView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdminRole
    ]

    def get(self, request):

        users = User.objects.all().order_by("id")

        serializer = UserSerializer(
            users,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = CreateUserSerializer(
            data=request.data
        )

        if serializer.is_valid():

            user = serializer.save()

            return Response(
                UserSerializer(user).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )   
    
class ResourceListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        resources = Resource.objects.all().order_by("name")

        serializer = ResourceSerializer(
            resources,
            many=True
        )

        return Response(serializer.data)
    
class ResourceDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, resource_id):

        resource = get_object_or_404(
            Resource,
            id=resource_id
        )

        latest = (
            MetricData.objects
            .filter(resource=resource)
            .order_by("-timestamp")
            .first()
        )

        return Response({

            "id": resource.id,

            "name": resource.name,

            "resource_type": resource.resource_type,

            "environment": resource.environment,

            "status": latest.status if latest else "UNKNOWN",

            "last_updated": (
                latest.timestamp
                if latest
                else None
            )

        })