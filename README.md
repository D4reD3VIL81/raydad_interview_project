# raydad interview project
It's an API for Create, View, Delete, and Updating the houses, It uses JWT Token for authentication.

## Setup
I've used `poetry` package manager for dependencies and it also has a Dockerfile for deployment.
Use `poetry install` to install the packages and use `poetry shell` for getting into enviroment.
You can run `python manage.py runserver` (make sure to migrate before running the server) and `python manage.py test` for the app tests.

## Instructions
API urls:
 - api/ houses/
 - api/ houses/user/ [name='list-user-houses']
 - api/ houses/user/create/ [name='create-user-house']
 - api/ houses/user/<int:pk>/delete/ [name='delete-user-house']
 - api/ houses/user/<int:pk>/update/ [name='update-user-house']
 - api/ houses/city/<str:city>/ [name='list-city-houses']
Auth urls:
 - auth/ ^jwt/create/? [name='jwt-create']
 - auth/ ^jwt/refresh/? [name='jwt-refresh']
 - auth/ ^jwt/verify/? [name='jwt-verify']
