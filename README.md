# Mini DevOps Platform

A DevOps learning project built with Docker Compose, Nginx, Flask, and PostgreSQL.

This project demonstrates a containerized application stack with a reverse proxy, backend API, database service, health checks, persistent storage, and environment-based configuration.

## Services

- Nginx Reverse Proxy: Routes client requests to frontend and backend services
- Frontend: Static HTML served by Nginx
- Backend: Flask API service
- PostgreSQL: Database with persistent volume storage

## Technologies Used

- Docker
- Docker Compose
- Nginx
- Flask
- PostgreSQL
- Git
- GitHub

## Features

- Docker Compose multi-service stack
- Nginx reverse proxy configuration
- Flask backend service
- PostgreSQL database integration
- Health checks for backend and database
- Persistent Docker volumes
- Environment variable configuration
- Database backup and restore strategy

## Architecture

```text
Client
  |
  v
Nginx Reverse Proxy
  |
  +--> Frontend
  |
  +--> Backend API
          |
          v
     PostgreSQL Database
```

## Getting Started

### 1. Clone the repository

```bash
git clone git@github.com:majidn72/mini-devops-platform.git
cd mini-devops-platform
```
### 2. Create environment file

Create a .env file based on your local configuration.

### 3. Start the services

```bash
docker compose up -d
```
### 4. Check running services

```bash
docker compose ps
```
### 5. View logs

```bash
docker compose logs -f
```
## Useful Commands

Rebuild the backend image without cache:

```bash
docker compose build --no-cache backend
docker compose up -d --force-recreate backend
```
Stop the stack:

```bash
docker compose down
```
Stop the stack and remove volumes:

```bash
docker compose down -v
```
> Warning: `docker compose down -v` removes the PostgreSQL volume and deletes database data.

## Database Backup

Create a database backup:

```bash
docker exec postgres-db pg_dump -U devops -d appdb > backup.sql
```
Restore a database backup:

```bash
docker exec -i postgres-db psql -U devops -d appdb < backup.sql
```
## Roadmap

* [x] Docker Compose Stack
* [x] Nginx Reverse Proxy
* [x] PostgreSQL Integration
* [x] Health Checks
* [x] Persistent Volumes
* [x] Backup and Restore Strategy
* [ ] CI/CD Pipeline
* [ ] VPS Deployment
* [ ] Monitoring with Prometheus & Grafana
* [ ] Kubernetes Migration
