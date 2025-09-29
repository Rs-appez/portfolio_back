from .models import Project, Tag, Image
from .serializers import ProjectSerializer, TagSerializer, ImageSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions


class ProjectViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TagViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ImageViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
