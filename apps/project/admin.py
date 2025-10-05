from django.contrib import admin
from .models import Project, Tag, Image

admin.site.register(Tag)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 3


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "linked_projects":
            if request.resolver_match and request.resolver_match.kwargs.get(
                "object_id"
            ):
                try:
                    obj_id = int(request.resolver_match.kwargs["object_id"])
                    kwargs["queryset"] = Project.objects.exclude(pk=obj_id)
                except (ValueError, TypeError):
                    pass
        return super().formfield_for_manytomany(db_field, request, **kwargs)
