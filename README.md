# Agentic Test Run Analytics Dashboard

A production-ready, containerized full-stack web application designed to aggregate, analyze, and monitor automated test run execution metrics. Engineered with a high-performance asynchronous Python backend, a state-driven reactive Vue 3 frontend, and automated CI/CD pipelines deployed directly to AWS.

## Live Demo

- Frontend Dashboard: `http://13.60.61.169:8080`
- Interactive API Documentation (Swagger UI): `http://13.60.61.169:8000/docs`

## Architecture & Tech Stack

The system is built on a highly decoupled, modern service architecture engineered for horizontal scalability and strict environment parity.

### Backend Engine

- FastAPI: Asynchronous, high-performance Python web framework for low-latency API routing.
- SQLAlchemy 2.0: Async ORM mapping cleanly to relational entities.
- Pydantic v2: Compile-time and runtime data validation and serialization.
- Pytest & TestClient: Test suite covering endpoint integration and unit testing.

### Frontend Dashboard

- Vue 3 (Composition API): Reactive, component-driven user interface.
- TypeScript: Strong typing across the frontend data model layer.
- Pinia: Centralized, modular state management.
- Tailwind CSS: Utility-first CSS framework for responsive layouts.
- Vite: High-speed frontend build tooling.

### DevOps & Cloud Infrastructure

- Docker & Docker Compose: Multi-container orchestration ensuring environment parity between local development, CI pipelines, and production.
- Multi-Stage Builds: Optimized production Docker images using Nginx to serve static assets.
- GitHub Actions: Automated CI pipelines for linting, builds, and backend integration testing.
- AWS EC2: Cloud-hosted Linux virtual machine running production workloads.

## Repository Layout

```text
├── .github/workflows/   # CI/CD pipeline automation (GitHub Actions)
├── backend/             # Asynchronous FastAPI service
│   ├── app/             # Application source (API, models, database schemas)
│   ├── tests/           # Automated Pytest suite
│   ├── init_db.py       # Database initialization script
│   └── requirements.txt # Python dependencies
└── frontend/            # Vue 3 / TypeScript UI
    ├── src/             # Vue components, Pinia stores, and views
    ├── package.json     # Node.js dependencies
    └── nginx.conf       # Production Nginx configuration
```

## Local Development Setup

Ensure Docker and Docker Compose are installed.

### 1. Clone the Repository and Start the Stack

```bash
git clone https://github.com/RuturajKotwal/agentic-test-dashboard.git
cd agentic-test-dashboard
docker compose up -d --build
```

### 2. Initialize the Database Schema

Run the database initialization script inside the backend container:

```bash
docker exec -it agentic_backend python init_db.py
```

### 3. Access the Services

Frontend Interface:

```text
http://localhost:8080
```

Backend API Documentation:

```text
http://localhost:8000/docs
```

## Continuous Integration Pipeline

Every pull request or merge into the `main` branch automatically triggers the GitHub Actions workflow located at:

```text
.github/workflows/ci.yml
```

The CI runner performs the following tasks:

- Frontend type checking and production builds using Node.js.
- Python backend dependency installation and validation.
- Automated integration testing using Pytest with an isolated SQLite configuration.
- Verification that application changes pass quality checks before deployment.