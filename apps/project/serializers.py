from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Project, Tag, Image


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "image"]


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class ProjectSerializer(ModelSerializer):
    images = ImageSerializer(many=True)
    tags = TagSerializer(many=True, read_only=True)
    tags_ids = PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, write_only=True, source="tags"
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "github_link",
            "live_link",
            "tags",
            "tags_ids",
            "images",
            "placeholder_image",
        ]
