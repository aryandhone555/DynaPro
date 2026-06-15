from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from metrics.models import MetricData


class Command(BaseCommand):

    help = "Delete metric data older than retention period"

    def add_arguments(self, parser):

        parser.add_argument(
            "--days",
            type=int,
            default=15
        )

    def handle(self, *args, **options):

        retention_days = options["days"]

        cutoff_date = timezone.now() - timedelta(
            days=retention_days
        )

        deleted_count, _ = (
            MetricData.objects
            .filter(timestamp__lt=cutoff_date)
            .delete()
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Deleted {deleted_count} records older than "
                f"{retention_days} days"
            )
        )