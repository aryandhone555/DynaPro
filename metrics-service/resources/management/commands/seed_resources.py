from django.core.management.base import BaseCommand
from resources.models import Resource


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        resources = [

            ("Payment Service", "APP"),
            ("User Service", "APP"),
            ("Transaction Service", "APP"),
            ("Notification Service", "APP"),
            ("Fraud Detection Service", "APP"),

            ("Primary PostgreSQL", "DB"),
            ("Replica PostgreSQL", "DB"),
        ]

        for name, rtype in resources:

            Resource.objects.get_or_create(
                name=name,
                resource_type=rtype
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Resources seeded successfully"
            )
        )
