# Task Manager API

REST API for task management built with FastAPI and PostgreSQL.

## Live Demo

API available at: https://task-manager-api-production-1862.up.railway.app

Interactive documentation: https://task-manager-api-production-1862.up.railway.app/docs

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
- Python 3.12+

### Run the project

```bash
# Clone the repository
git clone git@github.com:vanDevBett/task-manager-api.git
cd task-manager-api
```

```bash
# Create the environment file
cp .env.example .env
```

```bash
# Create and activate virtual environment

# Mac / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

```bash
# Start the containers
docker compose up --build
```

API available at `http://localhost:8000`

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
