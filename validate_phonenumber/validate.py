# Program to check whether a phone number is valid or not
import phonenumbers
from test import number
# Parsing String to Phone number
phone_number = phonenumbers.parse(number)

# Validating a phone number
valid = phonenumbers.is_valid_number(phone_number)

# Checking possibility of a number
possible = phonenumbers.is_possible_number(phone_number)

# Printing the output
print(valid)
print(possible)
