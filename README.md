# SecureEye

SecureEye is a Django-based project designed to stream multiple RTSP cameras and display the live feed on a web interface. The system allows users to add, list, and stream cameras through a REST API.

## Features

- **Manage Cameras**: Add and list multiple cameras via an API.
- **Live Streaming**: Stream live video feeds from RTSP cameras.
- **Django REST Framework**: Provides API endpoints for managing cameras.
- **Web Interface**: Displays live streams in a Django template.

## Requirements

- Docker
- Docker Compose
- Python 3.11+
- PostgreSQL 15
- OpenCV (for handling RTSP streams)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/secureeye.git
   cd secureeye
   ```

2. Create an `.env` file with the database credentials:

   ```env
   POSTGRES_DB=secureeye
   POSTGRES_USER=secureeye_user
   POSTGRES_PASSWORD=secureeye_password
   ```

3. Build and run the application:

   ```bash
   docker-compose up --build
   ```

4. The application will be available at:
   ```
   http://127.0.0.1:8000/
   ```

## API Endpoints

### List and Create Cameras

- **Endpoint:** `GET /cameras/api/cameras/`
- **Endpoint:** `POST /cameras/api/cameras/`
- **Description:** Retrieve a list of cameras or add a new one.

### Get Camera Details

- **Endpoint:** `GET /cameras/api/cameras/<int:pk>/`
- **Description:** Retrieve details of a specific camera.

### Stream Camera

- **Endpoint:** `GET /cameras/api/cameras/stream/<int:pk>/`
- **Description:** Stream the live feed of a specific camera.

## Viewing Streams

Visit the web interface at:

```
http://127.0.0.1:8000/cameras/view/
```

This page displays all registered camera streams.

## Troubleshooting

- **Database Connection Issues:** Ensure that PostgreSQL is running and `DATABASE_URL` is correctly set.
- **RTSP Stream Not Loading:** Confirm that the camera is accessible via the RTSP URL and that OpenCV is correctly installed.
- **Containers Not Starting:** Try rebuilding:
  ```bash
  docker-compose down
  docker-compose up --build
  ```

## License

This project is licensed under the MIT License.

## Authors

- Bryan Gallo
