# JokesAPI
This repo is just to show how to do a simple rest api with DRF, using docker and docker compose

This guide provides step-by-step instructions to clone the repository and run the Django REST API using Docker and Docker Compose.
By following these steps, you'll have the API up and running on your local machine.

Steps

1. Clone the Repository
   git clone <your-repository-url>

   cd your-repo-name

2. Build the Docker Image
   Using docker componse commands:
   - docker-compose build
   - docker-compose up
   If you want to see logs of the container
   - docker compose logs -f

3. Access the API

   Once the application is running, you can access the API endpoints via your web browser or an API client like Postman.

   Base URL: http://localhost:8000/api/jokes/

   You can test differents HTTP method as GET, POST, PUT and DELETE
   For GET method:
   curl -X GET http://localhost:8000/api/jokes/
   curl -X GET "http://localhost:8000/api/jokes/?query=Chuck"

  For POST method you have to pass a JSON body containing description key
  {"description": "Why do programmers prefer dark mode? Because light attracts bugs."}

  For PUT method you have to pass the id joke and the description that update the specific joke by the given id
  {"id": 1, "description": "Why do programmers prefer dark mode? Because light attracts bugs."}

  Finally, for DELETE method pass the id number in query params
  curl -X DELETE "http://localhost:8000/api/jokes/?number=1"


