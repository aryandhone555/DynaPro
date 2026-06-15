from django.core.management.base import BaseCommand

from simulator.services.orchestrator import (
    run_simulation
)
import time


class Command(BaseCommand):

    help = "Generate metric datapoints continuously"

    def handle(self, *args, **kwargs):

        self.stdout.write(
            self.style.SUCCESS(
                "Simulator started..."
            )
        )

        while True:

            count = run_simulation()

            self.stdout.write(
                self.style.SUCCESS(
                    f"{count} metric records created"
                )
            )

            time.sleep(10)