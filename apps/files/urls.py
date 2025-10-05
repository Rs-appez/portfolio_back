from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CVViewSet

router = DefaultRouter()
router.register(r"resume", CVViewSet, basename="cv")
urlpatterns = [path("api/", include(router.urls))]
