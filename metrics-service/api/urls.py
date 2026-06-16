from django.urls import path


from .views import (
    ResourceListView,
    ResourceMetricsView,
    MetricDataView,
    DashboardSummaryView,
    TopOffendersView,
    DashboardTrendView,
    ResourceHealthView
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
    path(
    "dashboard/top-offenders/",
    TopOffendersView.as_view(),
    name="top-offenders"
    ),
    path(
    "dashboard/trends/",
    DashboardTrendView.as_view(),
    name="dashboard-trends"
    ),
    path(
    "dashboard/resource-health/",
    ResourceHealthView.as_view(),
    name="resource-health"
    ),

]

