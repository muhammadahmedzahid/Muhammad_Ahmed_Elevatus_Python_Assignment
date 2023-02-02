# Muhammad_Ahmed_Elevatus_Python_Assignment
With these two files in place, you can build and run the Docker container using the following commands:
##### Build the Docker image
docker-compose build

##### Start the Docker container
docker-compose up<br/>
This will start the FastAPI application in a Docker container and make it accessible at http://localhost:8000 on your local machine.

##### Postman Collection is attached for testing routes:
Directly import the Elevatus Technical Assignment Collection.postman_collection inside postman.

#### About Saving Credentails in .env
I commit the code with the .env and also database connection in file because for testing purposes. But for production we place the keys in .env and initialze on environment variable.

#### User Authentication:
http://127.0.0.1:8000/candidate (GET, POST, DELETE, UPDATE)
http://127.0.0.1:8000/all_candidates (GET)
http://127.0.0.1:8000/generate_report (GET)

These endpoints are protected with Authorization JWT token which is generated from below endpoint for new users.
http://127.0.0.1:8000/user/signup {For user creation}
http://127.0.0.1:8000/user/signin {For generating tokens}
