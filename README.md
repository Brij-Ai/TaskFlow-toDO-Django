# ToDo — Django

A simple task management web application built with **Django**. Users can create, view, update, and delete their own tasks through an authenticated interface.

## Features

* User authentication
* Create tasks
* View tasks
* Update tasks
* Delete tasks
* Users can edit and delete only their own tasks
* Django template-based UI
* SQLite database

## Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML, CSS
* **Database:** SQLite
* **Environment:** Python Virtual Environment
* **Version Control:** Git & GitHub

## Setup

Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

Create and activate the virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Authentication

The application uses Django's built-in authentication system to manage user accounts and restrict task modification to their respective owners.

## Database

The project uses **SQLite** for development and local data storage.

## License

This project is intended for learning and development purposes.
