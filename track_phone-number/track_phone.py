# Tracking the phone numbers: finding the region and service name 

import phonenumbers
from phonenumbers import geocoder, carrier
from test import number

# Parsing string to phoneNumber
phoneNumber = phonenumbers.parse(number, 'CH')

# Getting carrier of phone
Carrier = carrier.name_for_number(phoneNumber, 'en')

# Getting region info
Region = geocoder.description_for_number(phoneNumber, 'en')

# print carrier and region
print(Carrier)
print(Region)
