from django.core.management.base import BaseCommand

from simulator.services.orchestrator import (
    run_simulation
)


class Command(BaseCommand):

    help = "Generate metric datapoints"

    def handle(self, *args, **kwargs):

        count = run_simulation()

        self.stdout.write(
            self.style.SUCCESS(
                f"{count} metric records created"
            )
        )

