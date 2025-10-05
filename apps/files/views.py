from .models import CV
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from .serializers import CVSerializer


class CVViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = CV.objects.all()
    serializer_class = CVSerializer
