from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from resources.models import Resource
from metrics.models import (
    MetricDefinition,
    MetricData
)

from simulator.services.generators import (
    generate_app_metric,
    generate_db_metric
)

from simulator.services.status import (
    calculate_status
)


class Command(BaseCommand):

    help = "Generate historical metric data"

    def add_arguments(self, parser):

        parser.add_argument(
            "--days",
            type=int,
            default=7
        )

    def handle(self, *args, **options):

        days = options["days"]

        end_time = timezone.now()

        start_time = end_time - timedelta(
            days=days
        )

        resources = Resource.objects.filter(
            is_active=True
        )

        records = []

        total_created = 0

        current_time = start_time

        self.stdout.write(
            self.style.SUCCESS(
                f"Generating {days} days of history..."
            )
        )

        while current_time <= end_time:

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
                            timestamp=current_time
                        )
                    )

                    if len(records) >= 5000:

                        MetricData.objects.bulk_create(
                            records,
                            batch_size=5000
                        )

                        total_created += len(records)

                        self.stdout.write(
                            f"Inserted {total_created} records..."
                        )

                        records = []

            current_time += timedelta(
                minutes=1
            )

        if records:

            MetricData.objects.bulk_create(
                records,
                batch_size=5000
            )

            total_created += len(records)

        self.stdout.write(
            self.style.SUCCESS(
                f"Finished. Generated {total_created} records."
            )
        )