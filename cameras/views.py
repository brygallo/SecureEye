from rest_framework import generics
from django.views.generic import TemplateView
from .models import Camera
from .serializers import CameraSerializer

from django.http import JsonResponse, StreamingHttpResponse
from django.views import View
from .models import Camera
from .stream import RTSPStream
import cv2

streams = {}

class CameraListCreateView(generics.ListCreateAPIView):
    """
    API View to list all active cameras and create new ones.
    """
    queryset = Camera.objects.filter(is_active=True)
    serializer_class = CameraSerializer

class CameraDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API View to retrieve, update, or delete a camera.
    """
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class CameraStreamView(TemplateView):
    """
    Renders the HTML page with camera streams.
    """
    template_name = "cameras/camera_stream.html"

    def get_context_data(self, **kwargs):
        """
        Adds all available cameras to the template context.
        """
        context = super().get_context_data(**kwargs)
        context["cameras"] = Camera.objects.all()
        return context



class CameraStreamAPIView(View):
    """
    API View to stream the video feed from an RTSP camera.
    """

    def get(self, request, pk):
        try:
            camera = Camera.objects.get(pk=pk, is_active=True)
            return StreamingHttpResponse(self.generate_frames(camera.rtsp_url),
                                         content_type="multipart/x-mixed-replace; boundary=frame")
        except Camera.DoesNotExist:
            return JsonResponse({"error": "Camera not found"}, status=404)

    def generate_frames(self, rtsp_url):
        """ Generates frames from the RTSP stream. """
        if rtsp_url not in streams:
            streams[rtsp_url] = RTSPStream(rtsp_url)

        while True:
            frame = streams[rtsp_url].get_frame()
            if frame is not None:
                _, buffer = cv2.imencode(".jpg", frame)
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
                

