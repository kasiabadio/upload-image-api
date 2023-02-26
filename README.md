# Api for uploading images

## Table of contents

- General info
- Setup
- Technologies

## General info

The purpose was to create django REST api for uploading images to the page.

# Setup

- Open terminal and go to folder upload_image
- Activate virtual environment: env\scripts\activate
- Install requirements: pip install -r requirements.txt
- Type in:
  - py manage.py makemigrations
  - py manage.py migrate
- To access functionality, one must be logged in. Create admin in console, py manage.py createsuperuser
- Run server: py manage.py runserver
- Log in
- To view users go to /users subpage and to view images, go to /images

## Technologies

- Django REST framework
- venv
