from django.db import models

class Camera(models.Model):
    """
    Model representing an RTSP camera.
    """
    name = models.CharField(max_length=100, unique=True)
    rtsp_url = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
