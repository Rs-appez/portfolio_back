from django.contrib import admin
from .models import CV


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ("file", "uploaded_at")
    readonly_fields = ("uploaded_at",)
