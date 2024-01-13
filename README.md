# raydad interview project
It's an API for Create, View, Delete, and Updating the houses, It uses JWT Token for authentication.

## Setup
I've used `poetry` package manager for dependencies and it also has a Dockerfile for deployment.
Use `poetry install` to install the packages and use `poetry shell` for getting into enviroment.
You can run `python manage.py runserver` (make sure to migrate before running the server) and `python manage.py test` for the app tests.

## Instructions
API urls:
 - api/houses/ (All houses list, Login required)
 - api/houses/user/ (All current user's house-list, Login required)
 - api/houses/user/create/ (User creating a house)
 - api/houses/user/<int:pk>/delete/ (User deleting one of his own houses)
 - api/houses/user/<int:pk>/update/ (User updating one of his own houses)
 - api/houses/city/<str:city>/ (All houses within the given city, also login required)
   
Auth urls:
 - auth/jwt/create/
 - auth/jwt/refresh/
 - auth/jwt/verify/
