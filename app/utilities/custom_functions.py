def update_candidate(candidate_id,first_name, last_name, email, career_level, job_major, years_of_experience, degree_type, skills, \
                     nationality, city, salary, gender):
    candidate_ = {}
    if candidate_id is not None and candidate_id != '':
        candidate_['candidate_id'] = candidate_id
    if first_name is not None and first_name != '':
        candidate_['first_name'] = first_name
    if last_name is not None and last_name != '':
        candidate_['last_name'] = last_name
    if email is not None and email != '':
        candidate_['email'] = email
    if career_level is not None and career_level != '':
        candidate_['career_level'] = career_level
    if job_major is not None and job_major != '':
        candidate_['job_major'] = job_major
    if years_of_experience is not None and years_of_experience != '':
        candidate_['years_of_experience'] = years_of_experience
    if degree_type is not None and degree_type != '':
        candidate_['degree_type'] = degree_type
    if skills is not None and skills != '':
        candidate_['skills'] = skills
    if nationality is not None and nationality != '':
        candidate_['nationality'] = nationality
    if city is not None and city != '':
        candidate_['city'] = city
    if salary is not None and salary != '':
        candidate_['salary'] = salary
    if gender is not None and gender != '':
        candidate_['gender'] = gender
    return candidate_
