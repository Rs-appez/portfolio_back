from django.db import models
from portfolio.storage_backends import ProjectImagesStorage
from utils.nameHandler import rename_file_to_upload


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Image(models.Model):
    project = models.ForeignKey(
        "Project", on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(
        upload_to=rename_file_to_upload,
        storage=ProjectImagesStorage(),
        blank=True,
        null=True,
    )
    legend = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return getattr(self.image, "url", "No Image") if self.image else "No Image"


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="projects")
    placeholder_image = models.ImageField(
        upload_to=rename_file_to_upload,
        storage=ProjectImagesStorage(),
        blank=True,
        null=True,
    )
    linked_projects = models.ManyToManyField("self", blank=True, symmetrical=True)

    def __str__(self):
        return f"{self.name}"
