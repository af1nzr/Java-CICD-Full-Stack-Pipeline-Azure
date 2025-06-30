# Full-App-Docker-acr-aci-Deploy

A full-stack, containerized application demonstrating a modern deployment pipeline using Docker, Azure Container Registry (ACR), and Azure Container Instances (ACI). This project features a Python Flask backend, a Spring Boot (Java) static frontend, and a MySQL database, all orchestrated with Docker Compose.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contribution](#contribution)
- [License](#license)

---

## Project Overview
This repository provides a template for deploying a multi-service application using Docker and Azure services. It is designed for rapid prototyping, DevOps demonstrations, and as a starting point for scalable cloud-native solutions.

- **Frontend:** Serves static content using Spring Boot and Nginx.
- **Backend:** Python Flask API with MySQL database connectivity.
- **Database:** MySQL with an initialization script for demo data.

---

## Architecture
```
[ Nginx (Frontend) ]  <-->  [ Flask (Backend API) ]  <-->  [ MySQL (Database) ]
```
- All services are containerized and communicate over a Docker network.
- Health checks and dependencies are managed via Docker Compose.
- Designed for seamless deployment to Azure using ACR and ACI.

---

## Tech Stack
- **Frontend:**
  - Java 17, Spring Boot 3.2.0 (serves static HTML)
  - Nginx (Dockerized static file server)
- **Backend:**
  - Python 3.9, Flask
  - MySQL Connector for Python
- **Database:**
  - MySQL 8.0 (Docker Compose)
  - Custom initialization via `init.sql`
- **DevOps/Deployment:**
  - Docker, Docker Compose
  - Azure Container Registry (ACR)
  - Azure Container Instances (ACI)

---

## Project Structure
```
backend/
  app.py                # Flask API
  requirements.txt      # Python dependencies
  Dockerfile            # Backend container

db/
  init.sql              # MySQL schema & seed data
  Dockerfile            # MySQL custom image (env setup)

frontend/
  src/main/java/com/af1n/FrontendApplication.java  # Spring Boot entry
  src/main/resources/static/index.html             # Static HTML
  Dockerfile            # Nginx static server
  pom.xml               # Java dependencies

docker-compose.yml      # Multi-service orchestration
README.md               # Project documentation
```

---

## Setup & Installation

### Prerequisites
- Docker & Docker Compose installed
- (Optional) Azure CLI for deployment

### Local Development
1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd Full-App-Docker-acr-aci-Deploy
   ```
2. **Build and start all services:**
   ```sh
   docker-compose up --build
   ```
3. **Access the services:**
   - Frontend: [http://localhost](http://localhost)
   - Backend API: [http://localhost:5001](http://localhost:5001)
   - Database: MySQL on port 3306 (internal)

### Stopping Services
```sh
docker-compose down
```

---

## Usage
- The frontend serves a static HTML page via Nginx and Spring Boot.
- The backend exposes two endpoints:
  - `/` : Returns a hello message from Flask.
  - `/db` : Connects to MySQL and returns the current database time.
- The database is pre-populated with demo users (see `db/init.sql`).

---

## Deployment

### Azure Container Registry (ACR) & Azure Container Instances (ACI)
1. **Build and tag images:**
   ```sh
   docker-compose build
   # Tag and push each image to your ACR
   ```
2. **Push images to ACR:**
   ```sh
   az acr login --name <your-acr-name>
   docker tag <local-image> <acr-name>.azurecr.io/<image>:<tag>
   docker push <acr-name>.azurecr.io/<image>:<tag>
   ```
3. **Deploy to ACI:**
   - Use Azure CLI or GitHub Actions to deploy containers from ACR to ACI.
   - Example GitHub Actions workflow can be added for CI/CD automation.

---

## Contribution
Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

---

## License
This project is licensed under the MIT License.
