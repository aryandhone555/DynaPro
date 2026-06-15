from django.core.management.base import BaseCommand


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

        self.stdout.write(
            self.style.SUCCESS(
                f"Generating {days} days of history..."
            )
        )