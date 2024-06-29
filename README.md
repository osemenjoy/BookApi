API DOCUMENTATION LINK: https://bookapi-pb21.onrender.com/api/schema/redoc/

# Django Project Setup Guide

This guide will walk you through setting up and running a Django application locally.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python (>=3.6)
- pip (Python package installer)
- PostgreSQL
- virtualenv (optional but recommended)

## 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/osemenjoy/BookApi.git
cd your-repository
```

## 2. Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 4. Set Up PostgreSQL
Ensure PostgreSQL is installed and running. Create a database and a user for your Django project:
```bash
psql
CREATE DATABASE book_api;
CREATE USER api_user WITH PASSWORD 'api_password';
ALTER ROLE api-user SET client_encoding TO 'utf8';
ALTER ROLE api-user SET default_transaction_isolation TO 'read committed';
ALTER ROLE api_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE book_api TO api_user;
```

## 5. Configure Environment Variables
Create a .env file in the project root and add the following environment variables:
```python
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=postgres://api_user:api_password@127.0.0.1:5432/book_api
```

## 6. Apply migrations
Apply the database migrations to set up your database schema:
```bash
python manage.py migrate
```

## 7. Create a Superuser
create a superuser to handle Django admin
```bash
python manage.py createsuperuser
```

## 8. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

## 9. Access the Admin Site
You can access the Django admin site at http://127.0.0.1:8000/admin/ using the superuser credentials you created.

## API Endpoints
Here are some of the key API endpoints available in the application:

Add a new book: POST /api/all_books/books/
Edit a book: PUT /api/all_books/books/{id}/
Delete a book: DELETE /api/all_books/books/{id}/
List all books: GET /api/all_books/books/
Check book availability: GET /api/all_books/books/{id}/check_availability/
Search books: GET /api/all_books/search_books/?{add query param}
API documentation: GET /api/schema/redoc/
Login Endpoint: POST api/login/
Registration for users: POST api/register/
refresh token: POST api/token/refresh/
