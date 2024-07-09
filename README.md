
## Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker is installed on your machine. If not, you can download it from [Docker](https://www.docker.com/get-started).

## Installing and Running

To install and run this project, follow these steps:

### Building the Docker Image

1. Open your terminal.
2. Clone the repository to your local machine (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
3. Build the Docker image:
   ```bash
   docker build -t my-app:latest .
   ```

### Running the Docker Container

Run the container using the following command:
```bash
docker run -p 8080:8080 --name my-running-app my-app:latest
```
This command does the following:
- `-p 8080:8080` maps port 8080 of the container to port 8080 on your host, allowing you to access the application via `localhost:8080`.
- `--name my-running-app` assigns the name `my-running-app` to your container instance.
- `my-app:latest` specifies the image to create the container from.

## Accessing the Application

Open a web browser and visit `http://localhost:8080` to access the application.

