# Task Manager API

## Features

- User Registration
- User Login
- JWT Authentication
- Password Hashing
- User-specific Task Management
- Create Task
- View Tasks
- Update Task
- Delete Task
- SQLite Database
- SQLAlchemy ORM
- Pydantic Validation

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

## API Documentation

http://127.0.0.1:8000/docs

## API Endpoints

### Authentication

- POST /auth/signup - Register a new user
- POST /auth/login - Login and receive JWT token
- GET /auth/me - Get logged-in user details

### Tasks

- POST /tasks - Create a task
- GET /tasks - Get all tasks of logged-in user
- PUT /tasks/{task_id} - Update a task
- DELETE /tasks/{task_id} - Delete a task

## Project Structure

```
task-manager-api/
│── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   ├── security.py
│   └── routes/
│       └── tasks.py
│
├── requirements.txt
├── tasks.db
└── README.md
```

## Technologies Used

- Python 3
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- JWT Authentication
- Passlib (Password Hashing)
- Uvicorn