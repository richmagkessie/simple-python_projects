# Program to extract phone numbers from a text
import phonenumbers

# Text Input
text = "Phone numbers are useful stuff and part of men. Everyday, i find numbers like +233548321529. I normally call +233246897501 and +233242983151"

# Pass the text and country code to the below function
numbers = phonenumbers.PhoneNumberMatcher(text, "IN")

# Printing the phone numbers matched with country code
# and also the indexes of the phone numbers in the string input
for number in numbers:
    print(number)
