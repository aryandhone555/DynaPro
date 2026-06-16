from django.urls import path


from .views import (
    ResourceListView,
    ResourceMetricsView,
    MetricDataView,
    DashboardSummaryView
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
    path(
    "dashboard/summary/",
    DashboardSummaryView.as_view(),
    name="dashboard-summary"
    ),

]

