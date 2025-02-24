# Online_courses

## Overview

This project is a Django API designed to manage online courses, lessons, and payments for users. It provides a structured way to create and manage educational content and track user payments. The project includes management commands to set up initial data, create test users, and generate payments for those users.

## Features

- **Course Management**: Create and manage courses.
- **Lesson Management**: Create and manage lessons associated with courses.
- **User Management**: Create test users for testing purposes.
- **Payment Management**: Generate and manage payments for users.

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
