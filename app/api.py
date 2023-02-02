from fastapi import FastAPI, Response, status, Depends
from .utilities import connect_db, email_validation, custom_functions
from .model import UserCreate, CandidateCreate, UserLogin, CandidateUpdate, CandidateSearch
import uuid
from operator import attrgetter
from .auth.auth_handler import signJWT
from .auth.auth_bearer import JWTBearer
from bson.objectid import ObjectId
import pandas as pd
from fastapi.responses import StreamingResponse
import io

app = FastAPI()


@app.post("/user/signup", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, response: Response) -> dict:
    first_name, last_name, email = attrgetter('first_name', 'last_name', 'email')(user)

    # TODO: Email Validation.
    email_validation_status = email_validation.email_validation(email)
    if 'error' in email_validation_status:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": email_validation_status['error']}

    # TODO: Checking if the first_name, last_name is present and non-empty.
    if first_name == '' or len(first_name) > 15 or last_name == '' or len(last_name) > 15:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": 'first_name and last_name must be present and length must be less than 15.'}

    # TODO: Connection with database.
    db_connection = connect_db.connect_with_mongodb()
    if 'error' in db_connection:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": db_connection['error']}
    try:
        db_collection = db_connection['message']
        user_collection = db_collection['user']
        # TODO: Check if user already exists
        if user_collection.find_one({"email": email}, {'_id': 0}):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"error": "Email already exists"}

        # TODO: Creating user in the database.
        user_id = str(uuid.uuid4())
        user = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "UUID": user_id
        }
        user_collection.insert_one(user)
        # Generating JWT Token using the email for production we need to pass email and password as well.
        return {"message": "User created successfully", "user": {"first_name": first_name,
                                                                 "last_name": last_name,
                                                                 "email": email,
                                                                 "UUID": user_id,
                                                                 "access_token": signJWT(user['email'])}}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}


@app.get("/user/signin", status_code=status.HTTP_200_OK)
async def create_user(response: Response, user: UserLogin = Depends()) -> dict:
    first_name, last_name, email = attrgetter('first_name', 'last_name', 'email')(user)

    # TODO: Email Validation.
    email_validation_status = email_validation.email_validation(email)
    if 'error' in email_validation_status:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": email_validation_status['error']}

    # TODO: Checking if the first_name, last_name is present and non-empty.
    if first_name == '' or len(first_name) > 15 or last_name == '' or len(last_name) > 15:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": 'first_name and last_name must be present and length must be less than 15.'}

    # TODO: Connection with database.
    db_connection = connect_db.connect_with_mongodb()
    if 'error' in db_connection:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": db_connection['error']}
    try:
        db_collection = db_connection['message']
        user_collection = db_collection['user']
        record_found = user_collection.find_one({"email": email, "first_name": first_name, "last_name": last_name})
        # TODO: Check if user already exists
        if record_found:
            print('Record Found:', record_found)
            # Generating JWT Token using the email for production we need to pass email and password as well.
            return {
                "user": {'id': str(record_found['_id']), "first_name": first_name, "last_name": last_name,
                         "email": email,
                         'UUID': record_found['UUID'],
                         "access_token": signJWT(email)}}
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"error": "Requested user does not exists. please check first_name, last_name and email."}

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}


@app.post("/candidate", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_201_CREATED)
async def create_candidate(candidate: CandidateCreate, response: Response) -> dict:
    first_name, last_name, email, career_level, job_major, years_of_experience, degree_type, skills, \
        nationality, city, salary, gender = attrgetter('first_name', 'last_name', 'email', 'career_level', 'job_major',
                                                       'years_of_experience', 'degree_type',
                                                       'skills', 'nationality', 'city', 'salary', 'gender')(candidate)

    first_name, last_name, email = candidate.first_name, candidate.last_name, candidate.email
    # TODO: Email Validation.
    email_validation_status = email_validation.email_validation(email)
    if 'error' in email_validation_status:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": email_validation_status['error']}

    # TODO: Checking if the first_name, last_name is present and non-empty.
    if first_name == '' or len(first_name) > 15 or last_name == '' or len(last_name) > 15:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": 'first_name and last_name must be present and length must be less than 15.'}

    # TODO: Connection with database.
    db_connection = connect_db.connect_with_mongodb()
    if 'error' in db_connection:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": db_connection['error']}
    try:
        db_collection = db_connection['message']
        candidate_collection = db_collection['candidate']
        # TODO: Check if user already exists
        if candidate_collection.find_one({"email": email}, {'_id': 0}):
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"error": "Candidate with the similar email already exists"}
        inserted_obj = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "UUID": str(uuid.uuid4()),
            "career_level": career_level,
            "job_major": job_major,
            "years_of_experience": years_of_experience,
            "degree_type": degree_type,
            "skills": skills,
            "nationality": nationality,
            "city": city,
            "salary": salary,
            "gender": gender
        }
        candidate_id = candidate_collection.insert_one(inserted_obj).inserted_id
        inserted_obj.update({"message": "Candidate created successfully"})
        inserted_obj['_id'] = str(inserted_obj['_id'])
        return inserted_obj
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}


@app.get("/candidate/{candidate_id}", dependencies=[Depends(JWTBearer())])
async def get_candidate(candidate_id: str, response: Response) -> dict:
    try:
        db_connection = connect_db.connect_with_mongodb()
        db_collection = db_connection['message']
        candidate_collection = db_collection['candidate']
        candidate = candidate_collection.find_one({"_id": ObjectId(candidate_id)})
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

    if candidate:
        candidate['_id'] = str(candidate['_id'])
        return candidate
    else:
        return {"message": f"Requesting candidate with id {candidate_id} not found"}


@app.patch("/candidate/{candidate_id}", dependencies=[Depends(JWTBearer())])
async def update_candidate(candidate_id: str, candidate: CandidateUpdate, response: Response) -> dict:
    first_name, last_name, career_level, job_major, years_of_experience, degree_type, skills, \
        nationality, city, salary, gender = attrgetter('first_name', 'last_name',
                                                       'career_level', 'job_major',
                                                       'years_of_experience', 'degree_type',
                                                       'skills', 'nationality', 'city', 'salary', 'gender')(candidate)
    try:
        db_connection = connect_db.connect_with_mongodb()
        db_collection = db_connection['message']
        candidate_collection = db_collection['candidate']
        is_candidate_exists_with_id = candidate_collection.find_one({"_id": ObjectId(candidate_id)})

        # TODO: Check if user already exists
        # It means some other candidate with the similar email exists.
        if is_candidate_exists_with_id is None:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {
                "error": f"Candidate does not exists with the requested id:{candidate_id}"}
        candidate_collection = db_collection['candidate']
        update_cand = custom_functions.update_candidate(None, first_name, last_name, None, career_level, job_major,
                                                        years_of_experience, degree_type, skills, \
                                                        nationality, city, salary, gender)
        print(update_cand)
        candidate_collection.update_one({"_id": ObjectId(candidate_id)}, {"$set": update_cand})

        return {"message": "Candidate updated with following details successfully", 'candidate': update_cand}
    except Exception as e:
        return {'error': str(e)}


@app.delete("/candidate/{candidate_id}", dependencies=[Depends(JWTBearer())])
async def get_candidate(candidate_id: str, response: Response) -> dict:
    try:
        db_connection = connect_db.connect_with_mongodb()
        db_collection = db_connection['message']
        candidate_collection = db_collection['candidate']
        candidate = candidate_collection.find_one({"_id": ObjectId(candidate_id)})
        if candidate:
            candidate_collection.delete_one({"_id": ObjectId(candidate_id)})
            return {'message': f'Candidate with {candidate_id} deleted successfully.'}
        else:
            return {'error': f"Candidate with {candidate_id} does not exists."}

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}


# async def create_user(response: Response, user: UserLogin = Depends()) -> dict:

@app.get("/all_candidates", dependencies=[Depends(JWTBearer())])
async def all_candidate(response: Response, candidate: CandidateSearch = Depends()) -> dict:
    try:
        candidate_id, first_name, last_name, email, career_level, job_major, years_of_experience, degree_type, skills, \
            nationality, city, salary, gender = attrgetter('candidate_id', 'first_name', 'last_name', 'email',
                                                           'career_level', 'job_major',
                                                           'years_of_experience', 'degree_type',
                                                           'skills', 'nationality', 'city', 'salary', 'gender')(
            candidate)
        db_connection = connect_db.connect_with_mongodb()
        db_collection = db_connection['message']
        candidate_collection = db_collection['candidate']
        candidate_search = custom_functions.update_candidate(candidate_id, first_name, last_name, email, career_level,
                                                             job_major, years_of_experience, degree_type, skills, \
                                                             nationality, city, salary, gender)
        print("candidate_search:", candidate_search)
        candidates = candidate_collection.find(candidate_search)
        candidates_list = []
        for can in candidates:
            can['_id'] = str(can['_id'])
            candidates_list.append(can)
        if len(candidates_list):
            return {'candidates': candidates_list}
        else:
            return {"message": f"Requesting candidates with Search criteria not found"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}


@app.get("/generate_report", dependencies=[Depends(JWTBearer())])
async def all_candidate(response: Response) -> dict:
    try:
        db_connection = connect_db.connect_with_mongodb()
        db_collection = db_connection['message']
        candidate_collection = db_collection['candidate']

        candidates = candidate_collection.find({}, {"_id": 0})
        candidates = [can for can in candidates]
        df = pd.DataFrame(candidates)
        stream = io.StringIO()
        df.to_csv(stream, index=False)

        response = StreamingResponse(iter([stream.getvalue()]),
                                     media_type="text/csv"
                                     )
        response.headers["Content-Disposition"] = "attachment; filename=export.csv"

        return response

    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
