
import re

'''
InputValidator Class
- Validates user inputs
'''
class InputValidator:
    '''
    Validate Email
    - Returns True if an email is valid, and False if it is not
    '''
    def validate_email(email: str):
        regex = r"[^@]+@[^@]+\.[^@]+"
        return re.match(regex, email)

    '''
    Validate Phone Number
    - Returns True if a phone number is valid, and False if it is not
    '''
    def validate_phone_number(phone_number: str):
        regex = r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
        return re.match(regex, phone_number)

