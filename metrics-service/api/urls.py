from django.urls import path


from .views import (
    ResourceListView,
    ResourceMetricsView,
    MetricDataView
)
urlpatterns = [

    path(
    "resources/<int:resource_id>/metrics/",
    ResourceMetricsView.as_view(),
    name="resource-metrics"
    ),
    path(
    "metric-data/",
    MetricDataView.as_view(),
    name="metric-data"
),

]

