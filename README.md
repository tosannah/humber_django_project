Waypoint

Waypoint is a Django web application for browsing and managing hiking
trails.

Setup

Create and activate the virtual environment:

python -m venv env

On Windows:

env\Scripts\activate

Install the project dependencies:

pip install -r requirements.txt

Database Setup

Apply the database migrations:

python manage.py migrate

Create a superuser for the Django admin:

python manage.py createsuperuser

Run the Application

Start the Django development server:

python manage.py runserver

Then open the application in your browser:

http://127.0.0.1:8000/

The public trail catalog is available at:

http://127.0.0.1:8000/trails/

The Django administration site is available at:

http://127.0.0.1:8000/admin/

Testing

Run the automated test suite with:

python manage.py test

The project includes tests for:

Open-trail filtering

Trail detail 404 handling

Invalid difficulty validation

Project Features

Django-based trail catalog

Trail and Park database models

Trail-to-Park ForeignKey relationship

Django admin management

Open/closed trail filtering

Park-based trail filtering

Trail detail pages

Automated tests

Screenshots

Trail Catalog



Django Admin