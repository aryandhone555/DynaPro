from django.utils import timezone
import time

from resources.models import Resource
from metrics.models import MetricDefinition, MetricData

from simulator.services.generators import (
    generate_app_metric,
    generate_db_metric
)

from simulator.services.status import (
    calculate_status
)


def run_simulation():

    resources = Resource.objects.filter(
        is_active=True
    )

    records = []   # ← Missing

    for resource in resources:

        metrics = MetricDefinition.objects.filter(
            resource_type=resource.resource_type
        )

        for metric in metrics:

            if resource.resource_type == "APP":

                value = generate_app_metric(
                    metric.name
                )

            else:

                value = generate_db_metric(
                    metric.name
                )

            status = calculate_status(
                value,
                metric.warning_threshold,
                metric.critical_threshold
            )

            records.append(
                MetricData(
                    resource=resource,
                    metric=metric,
                    value=value,
                    status=status,
                    timestamp=timezone.now()
                )
            )

    MetricData.objects.bulk_create(records)  # ← Missing

    return len(records)  # ← Better than records_created