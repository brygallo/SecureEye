from django.urls import path
from .views import CameraListCreateView, CameraDetailView, CameraStreamAPIView, CameraStreamView

urlpatterns = [
    path("api/cameras/", CameraListCreateView.as_view(), name="camera-list-create"),
    path("api/cameras/<int:pk>/", CameraDetailView.as_view(), name="camera-detail"),
    path("api/cameras/stream/<int:pk>/", CameraStreamAPIView.as_view(), name="camera-stream-api"),
    path("view/", CameraStreamView.as_view(), name="camera-stream"),
]
