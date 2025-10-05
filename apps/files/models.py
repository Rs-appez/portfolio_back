from django.db import models
from portfolio.storage_backends import CvStorage


class CV(models.Model):
    file = models.FileField(
        storage=CvStorage(),
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CV uploaded at {self.uploaded_at}"
