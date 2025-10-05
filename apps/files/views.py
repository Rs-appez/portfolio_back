from .models import CV
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CVSerializer


class CVViewSet(ModelViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = CV.objects.all()
    serializer_class = CVSerializer

    @action(detail=False, methods=["get"])
    def latest(self, request):
        latest_cv = CV.objects.latest("uploaded_at")
        serializer = self.get_serializer(latest_cv)
        return Response(serializer.data)
