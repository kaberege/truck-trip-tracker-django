
# Backend - Trip Log Application (Django)

This is the backend API for the Trip Log application, built with Django and Django REST Framework. The API allows users to input trip details and generate ELD logs and route instructions.

## Requirements

asgiref==3.8.1
Django==5.2
django-cors-headers==4.7.0
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
PyJWT==2.9.0
sqlparse==0.5.3
tzdata==2025.2
whitenoise==6.9.0

## Installation

### 1. Clone the Repository
```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Set Up Virtual Environment
Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Configure the Database
Run database migrations to set up the required tables:
```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)
Create a superuser to access the Django admin interface:
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

## API Endpoints
- **POST `/user/register/`** - Create a new user || create an account.
- **POST `/user/login/`** - Authenticate a user.
- **POST `/log/trips/`** - Create a new trip log.
- **GET `/log/trips/`** - Fetch all trip logs for the authenticated user.
- **GET `/log/trips/{id}/`** - Fetch a specific trip log.
- **PUT/PATCH `/log/trips/{id}/`** - Update a trip log.
- **DELETE `/log/trips/{id}/`** - Delete a trip log.

## Authentication
This API uses JWT (JSON Web Token) authentication. Users must log in and obtain a token to access protected endpoints.

## Testing the API

You can use tools like Postman or cURL to test the endpoints. Make sure to include the authentication token in the request headers as `Authorization: Bearer <your_token>`.
