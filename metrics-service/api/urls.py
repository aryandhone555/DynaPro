from django.urls import path


from .views import (
    ResourceListView,
    ResourceMetricsView
)
urlpatterns = [

    path(
    "resources/<int:resource_id>/metrics/",
    ResourceMetricsView.as_view(),
    name="resource-metrics"
    ),

]

