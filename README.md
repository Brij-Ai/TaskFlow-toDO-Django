# TaskFlow

A Django-based task management web application that helps users create, organize, prioritize, and track their tasks through an authenticated interface.

## Features

* User registration and authentication
* Create, view, update, and delete tasks
* Mark tasks as completed or pending
* Set task priorities
* User-specific task management
* Task search functionality
* Dashboard with task statistics
* Completion rate and progress tracking
* Recent tasks overview
* Contact Us form
* Bootstrap-based responsive UI
* Django messages for user feedback

## Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite
* **Environment:** Python Virtual Environment
* **Version Control:** Git & GitHub

## Project Structure

```text
TaskFlow/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── tasks/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    └── ...
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Brij-Ai/TaskFlow-Django.git
cd TaskFlow-Django
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application at:

```text
http://127.0.0.1:8000/
```

## Authentication

TaskFlow uses Django's built-in authentication system for user registration, login, and logout.

Each user's tasks are associated with their account, ensuring that users can manage only their own tasks.

## Dashboard

The dashboard provides an overview of task activity, including:

* Total tasks
* Pending tasks
* Completed tasks
* Completion rate
* Progress visualization
* Recent tasks

## Database

The project uses **SQLite** for development and local data storage.

## Learning Purpose

TaskFlow was developed as a practical project for learning Django concepts including:

* Django project and app structure
* Models and migrations
* Django ORM and QuerySets
* URL routing
* Views and templates
* Forms and POST requests
* Authentication and authorization
* CRUD operations
* Template context and template logic
* Django messages
* Bootstrap integration

## License

This project is intended for learning and development purposes.
