from email_validator import validate_email, EmailNotValidError


def email_validation(email):
    try:
        valid = validate_email(email)
        email = valid.email
        return {"message": email}
    except EmailNotValidError as e:
        return {"error": str(e)}
