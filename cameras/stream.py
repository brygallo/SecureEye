import cv2
from threading import Thread

class RTSPStream:
    """
    Handles RTSP stream capturing in a separate thread.
    """
    def __init__(self, rtsp_url):
        self.rtsp_url = rtsp_url
        self.cap = cv2.VideoCapture(self.rtsp_url)
        self.frame = None
        self.running = True
        Thread(target=self.update, daemon=True).start()

    def update(self):
        """ Continuously captures frames from the RTSP stream. """
        while self.running:
            success, frame = self.cap.read()
            if success:
                self.frame = frame

    def get_frame(self):
        """ Returns the last captured frame. """
        return self.frame

    def stop(self):
        """ Stops capturing and releases the camera. """
        self.running = False
        self.cap.release()
