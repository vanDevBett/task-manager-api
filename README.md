# Task Manager API

REST API for task management built with FastAPI and PostgreSQL.

## Tech Stack

- **FastAPI** — Python web framework
- **PostgreSQL** — Database
- **SQLAlchemy** — ORM
- **Pydantic** — Data validation
- **Docker** — Containerization
- **pytest** — Testing

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Run the project

```bash
# Clone the repository
git clone git@github.com:vanDevBett/task-manager-api.git
cd task-manager-api

# Create the environment file
cp .env.example .env

# Start the containers
docker compose up --build
```

The API will be available at `http://localhost:8000`

Interactive documentation at `http://localhost:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get a task by id |
| POST | /tasks | Create a task |
| PUT | /tasks/{id} | Update a task |
| DELETE | /tasks/{id} | Delete a task |

## Run Tests

```bash
pytest tests/ -v
```

## Project Structure

```
app/
├── api/          # Endpoints
├── core/         # Configuration and database
├── models/       # Database models
├── schemas/      # Pydantic schemas
├── services/     # Business logic
└── main.py       # Entry point
```