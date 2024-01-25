from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Contact management section for admin
    """
    list_display = (
        "date_created",
        "topic",
        "name",
        "email",
        "message",
        "status",
    )

    list_filter = ("date_created", "name", "topic", "status")

    ordering = ("-date_created",)

admin.site.register(Contact)
