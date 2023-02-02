#### Muhammad_Ahmed_Elevatus_Python_Assignment
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
Roles are protected using JWT tokens:<br/>
The generated token is valid for 10 minutes after 10 minutes you need to generate token again using the /signin endpoint.<br/>

http://127.0.0.1:8000/candidate (GET, POST, DELETE, UPDATE)<br/>
http://127.0.0.1:8000/all_candidates (GET)<br/>
http://127.0.0.1:8000/generate_report (GET)<br/>

These endpoints are protected with Authorization JWT token which is generated from below endpoint for new users.
http://127.0.0.1:8000/user/signup {For user creation}<br/>
http://127.0.0.1:8000/user/signin {For generating tokens}

Here are some screenshots:

![image](https://user-images.githubusercontent.com/54658973/216452873-0134e836-52d5-4a0e-a933-4031b1e0047a.png)


#### Creation of New User

![image](https://user-images.githubusercontent.com/54658973/216453112-c3b6dea5-18ea-44f7-b9a9-7837bb73ed76.png)
#### Error If you create user with the same email address
![image](https://user-images.githubusercontent.com/54658973/216453210-10e123ab-38d7-48e9-aa93-e81a4694a88f.png)

#### If you want to generate token after the expiration 

![image](https://user-images.githubusercontent.com/54658973/216453711-9a88e6aa-7e4c-4015-a3a5-25559e079d62.png)

#### If you want to generate the report in CSV. Here is the sample output
![image](https://user-images.githubusercontent.com/54658973/216453967-0d4906fb-0188-4d8a-a4bb-4fb672b24d94.png)

#### List the candidates with the search capabilites you can either any of the below:
- candidate_id
- first_name
- last_name
- email
- career_level
- job_major
- years_of_experience
- degree_type
- skills
- nationality
- city
- salary
- gender
![image](https://user-images.githubusercontent.com/54658973/216454240-b6072fe9-091f-44d3-90d8-8880d6fbc5dd.png)

