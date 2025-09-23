from django.db import models
from portfolio.storage_backends import ProjectImagesStorage
from utils.nameHandler import rename_file_to_upload


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(
        upload_to=rename_file_to_upload,
        storage=ProjectImagesStorage(),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.image.url if self.image else "No Image"


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="projects")
    placeholder_image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="placeholder_for",
    )
    images = models.ManyToManyField(Image, related_name="projects", blank=True)

    def __str__(self):
        return self.name
