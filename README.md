# Online_courses

## Overview

This project is a Django API designed to manage online courses, lessons, and payments for users. It provides a structured way to create and manage educational content and track user payments. The project includes management commands to set up initial data, create test users, and generate payments for those users.

# Project Setup Instructions

First of all, make sure you have Docker and Docker Compose installed on your machine.

## Running the Project with Docker Compose

Follow these steps to run the project using `docker-compose`:

1. **Clone the repository**:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create and configure the `.env` file**:
    ```sh
    cp .env.example .env
    # Edit the .env file to set your environment variables
    ```

3. **Build and start the Docker containers**:
    ```sh
    docker-compose up --build
    ```

## Starting the Project

To start the project on the background from scratch, use the following command:
```sh
docker-compose up -d --build
```

This command will build and start all the services defined in the `docker-compose.yml` file.

## Verifying Service Functionality

After starting the project, you can verify that all services are running correctly. The following commands will help you set up the initial data and test users:

- Create a superuser for the Django admin:
    ```sh
    docker-compose exec backend python manage.py createadmin
    ```
  login: admin@test.com
  password: adminpass

- Create test users:
    ```sh
    docker-compose exec backend python manage.py create_test_users
    ```

- Create courses and lessons:
    ```sh
    docker-compose exec backend python manage.py create_courses_and_lessons
    ```

#### It's convenient to use Postman for working with the API.

All url you can find in the `urls.py` file or by accessing the docs page at `http://localhost:8000/redoc/` or `http://localhost:8000/swagger/`.

- create a user with working e-mail address
- create a subscription for user with working e-mail address


To ensure each service is running correctly, follow these steps:

1. **Backend Service**:
    - Access the backend service by navigating to `http://localhost:8000` in your web browser.
    - Verify that the Django application is running.

2. **Database Service**:
    - Ensure the PostgreSQL database is running by checking the logs:
        ```sh
        docker-compose logs db
        ```
    - You should see logs indicating that the database is ready to accept connections.

3. **Redis Service**:
    - Ensure the Redis service is running by checking the logs:
        ```sh
        docker-compose logs redis
        ```
    - You should see logs indicating that Redis is ready to accept connections.

4. **Celery Worker**:
    - Ensure the Celery worker is running by checking the logs:
        ```sh
        docker-compose logs celery
        ```
    - Send a PUT or PATCH request for updating a course which has an active subscribed user
    - Such user should receive an email with notification
    - You should see logs indicating that the Celery worker is processing tasks.
     

5. **Celery Beat**:
    - Ensure the Celery beat scheduler is running by checking the logs:
        ```sh
        docker-compose logs celery-beat
        ```
    - Navigate to admin page and login as superuser
    - choose any active user and change "last login" field to the past date which is at least 30 days ago from current date
    - Celery beat task will set such user to inactive state (default task period is 1 day)
    - You should see logs indicating that the Celery beat scheduler is running.

By following these steps, you can verify that each service is functioning correctly.

## Features

- **Course Management**: Create and manage courses.
- **Lesson Management**: Create and manage lessons associated with courses.
- **User Management**: Create test users for testing purposes.
- **Payment Management**: Generate and manage payments for users.
- **Pagination for course listings**
- **Group-based permissions for moderators**
- **Subscription management**


## Setup

To set up the project, follow these steps:

1. **Create Courses and Lessons**: This command creates or retrieves the courses and lessons.

    ```bash
    python manage.py create_courses_and_lessons
    ```

2. **Create Test Users**: This command creates test users with email addresses starting with "user_".

    ```bash
    python manage.py create_test_users
    ```

3. **Create Payments**: This command creates payments for the test users, associating them with the created courses and lessons.

    ```bash
    python manage.py create_payments
    ```

## Usage

1. Run the `create_courses_and_lessons` command to set up the initial courses and lessons.
2. Run the `create_test_users` command to create the test users.
3. Run the `create_payments` command to generate payments for the test users.

By following these steps, you will have a fully set up environment with courses, lessons, test users, and associated payments.

## API Endpoints

### User Endpoints

- `POST /register/` - Register a new user
- `POST /login/` - Obtain a JWT token
- `POST /token/refresh/` - Refresh JWT token
- `GET /users/` - List all users
- `GET /users/<int:pk>/` - Retrieve a user
- `PUT /users/<int:pk>/update/` - Update a user
- `DELETE /users/<int:pk>/delete/` - Delete a user

### Course Endpoints

- `GET /courses/` - List all courses (paginated)
- `POST /courses/` - Create a new course
- `GET /courses/<int:pk>/` - Retrieve a course
- `PUT /courses/<int:pk>/` - Update a course
- `DELETE /courses/<int:pk>/` - Delete a course

### Lesson Endpoints

- `GET /lessons/` - List all lessons
- `POST /lessons/` - Create a new lesson
- `GET /lessons/<int:pk>/` - Retrieve a lesson
- `PUT /lessons/<int:pk>/` - Update a lesson
- `DELETE /lessons/<int:pk>/` - Delete a lesson


- ### Subscription Endpoints

- `POST /subscription/` - Subscribe or unsubscribe to a course

### Payment Endpoints

- `GET /payments/` - List all payments
- `POST /payments/` - Create a new payment

## Running Tests

To run the tests, use the following command:
```sh
python manage.py test