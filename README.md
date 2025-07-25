# Flask + MongoDB Docker Starter project

A production-ready Dockerized Python Flask application with MongoDB database and Mongo-Express admin UI.

## Features

- **Flask REST API** with Python 3.9
- **MongoDB 6.0+** with persistent storage
- **Mongo-Express** web UI for database management
- **Health checks** and dependency management
- **Docker Compose** orchestration

## Quick Start

### Prerequisites
- Docker 20.10+
- Docker Compose 2.0+

```
# Clone the repository
git clone https://github.com/Gokul-Nath-github/docker-flask-mongo-starter.git
cd flask-mongo-docker

# Start the stack
docker-compose up -d --build
```
## After building the services check the valid ports
 Flask app at port 5000
 Mongo db at port 27017
 Mongo-express ui at port 8081

## Stop all services by 
```
docker compose -f docker-setup
```
