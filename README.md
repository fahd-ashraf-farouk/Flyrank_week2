# Task and Library Management API (Task API)

Welcome to the Task API repository. This project is built as a professional Python package using the FastAPI framework. The project structure is organized within a dedicated source directory (src/) and managed using the configuration standards of pyproject.toml.

This API manages a simple in-memory library/task dictionary to demonstrate a complete CRUD (Create, Read, Update, Delete) lifecycle conforming to industry-standard development practices.

---

## Directory Structure

The repository follows the standard layout for modern Python packaging:

```text
├── pyproject.toml
├── README.md
└── src/
    └── task_api/
        ├── __init__.py
        └── main.py

```

---

## Installation and Setup

Since this project is structured as an installable Python package, you can set it up and run it locally with these steps:

### 1. Install the Project in Editable Mode

From the root directory of the project (where pyproject.toml is located), open your terminal and run:

```bash
pip install -e .

```

This command installs all required dependencies (FastAPI, Uvicorn, Pydantic) and registers your local package so it can be executed from anywhere.

### 2. Run the Development Server

Start the local server by pointing to the package path inside the src folder:

```bash
uvicorn task_api.main:app --reload

```

By default, the server will be live at: http://localhost:8000

---

## API Endpoints

The API conforms to RESTful standards and returns precise HTTP status codes:

| HTTP Method | Endpoint | Expected Status | Description |
| --- | --- | --- | --- |
| GET | / | 200 OK | General information about the API |
| GET | /health | 200 OK | Service health-check endpoint |
| GET | /tasks | 200 OK | Fetch all tasks/books in the library |
| GET | /tasks/{id} | 200 OK / 404 | Fetch a specific task by its ID |
| POST | /tasks | 201 Created / 422 | Create a new task with an auto-incrementing ID |
| PUT | /tasks/{id} | 200 OK / 404 | Update an entire existing task |
| DELETE | /tasks/{id} | 204 No Content / 404 | Permanently remove a task from the library |

---

## Local testing examples using curl

### 1. Retrieve all tasks (GET /tasks)

```bash
curl -i http://localhost:8000/tasks

```

**Expected Response (200 OK):**

```http
HTTP/1.1 200 OK
content-type: application/json

[
  {"id": 0, "title": "Python1", "author": "fahd", "lines": 15},
  {"id": 1, "title": "fast api", "author": "fahd ", "lines": 50}
]

```

### 2. Create a new task (POST /tasks)

```bash
curl -i -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Build a CLI tool", "author": "fahd", "lines": 120}'

```

**Expected Response (201 Created):**

```http
HTTP/1.1 201 Created
content-type: application/json

{"id": 2, "title": "Build a CLI tool", "author": "fahd", "lines": 120}

```

### 3. Request a non-existent task (GET /tasks/99)

```bash
curl -i http://localhost:8000/tasks/99

```

**Expected Response (404 Not Found):**

```http
HTTP/1.1 404 Not Found
content-type: application/json

{"detail": "Task with id 99 not found"}

```

---

## Interactive Documentation (Swagger UI)

FastAPI automatically generates interactive Swagger UI documentation for your project out-of-the-box:

* Run the server and visit: http://localhost:8000/docs in your browser.
* You can visualize models, review payload expectations, and test all CRUD operations directly via the interactive "Try it out" feature.

(You can replace this text with a screenshot of your Swagger UI interface)

---

## The Mortality Experiment

**Observation and Conclusion:**
Because this application uses a local Python dictionary (library = {}) stored entirely in volatile memory (In-memory storage), stopping (Ctrl + C) or restarting the server immediately wipes out any tasks created, updated, or deleted during runtime.

The application reverts to its hardcoded seeds (0 and 1) upon startup. This illustrates the critical need for Persistent Databases (such as PostgreSQL, MySQL, or SQLite) to preserve state and keep application data safe across restarts.

---
### Author

#### Fahd Ashraf Farouk
