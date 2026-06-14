from django.contrib import admin
from .models import Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "resource_type",
        "environment",
        "is_active",
    )

    list_filter = (
        "resource_type",
        "environment",
        "is_active",
    )

    search_fields = (
        "name",
    )