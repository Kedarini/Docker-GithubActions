# Multi-Container App with Docker, Nginx & GitHub Actions

A multi-service web application fully containerized with Docker and orchestrated using Docker Compose. The stack consists of a frontend, a FastAPI backend, and a PostgreSQL database, all routed through **Nginx as a reverse proxy**. A GitHub Actions workflow is used to validate that the entire stack builds successfully on every push and pull request.

## Tech Stack

| Layer | Technology |
| :-- | :-- |
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) (Python) |
| **Database** | [PostgreSQL](https://www.postgresql.org/) |
| **Reverse Proxy** | [Nginx](https://nginx.org/) |
| **Containerization** | [Docker](https://www.docker.com/), [Docker Compose](https://docs.docker.com/compose/) |
| **CI/CD** | [GitHub Actions](https://github.com/features/actions) |

## Architecture

```text
[Client] → [Nginx (Reverse Proxy :80)] → [Frontend] / [FastAPI Backend]
                                              ↓
                                           [PostgreSQL]
- Nginx acts as the single entry point for the application, routing incoming requests to the appropriate service.
- Frontend and FastAPI run in separate containers and communicate over an internal Docker network.
- PostgreSQL is used as the persistent database, with its data stored in a dedicated Docker volume.
- All services are connected through a shared network created automatically by docker-compose.yml.
Features
- Multi-container setup – Each component runs in its own isolated container.
- Nginx reverse proxy – Clean, unified access to both the frontend and API through port 80.
- Service orchestration – Entire stack spun up and torn down with a single command.
- Internal networking – Services communicate securely over Docker's internal network.
- CI build validation – GitHub Actions ensures all Docker images build correctly on every change.
Getting Started
Prerequisites
- Docker
- Docker Compose
Run Locally
1. Clone the repository
git clone https://github.com/Kedarini/Docker-GithubActions.git
cd Docker-GithubActions
2. Create an environment file
cp .env.example .env
Update the values in .env to match your configuration if needed.
3. Build and start the stack
docker compose up --build
4. Access the application
Open http://localhost in your browser.
5. Stop the stack
docker compose down
To also remove the database volume: 
docker compose down -v
Environment Variables
Create a .env.example file in the root of the repository with the following values:
POSTGRES_DB=app_db
POSTGRES_USER=app_user
POSTGRES_PASSWORD=app_password
DATABASE_URL=postgresql://app_user:app_password@db:5432/app_db
Note: Never commit your real .env file to Git. Only keep .env.example in the repository.
CI/CD
This repository includes a GitHub Actions workflow located in .github/workflows/. On every push and pull request, it runs docker compose build to validate that all services can be built successfully. This ensures configuration errors in Dockerfile or docker-compose.yml are caught early.
Project Goals
The main goal of this project was to get hands-on with multi-container orchestration, Nginx reverse proxy configuration, inter-container networking and basic CI build validation with GitHub Actions. 
License
This project is licensed under the MIT License.
