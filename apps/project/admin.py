from django.contrib import admin
from .models import Project, Tag, Image

admin.site.register(Tag)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

