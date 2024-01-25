import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

# Taking a number from the user: 
num = input("Enter the a number in the format <+countrycode with number>: ")

# phonenumbers.parse(): Function to seperate the number and the country code
mynum = phonenumbers.parse(num)
print("Country Code: ", mynum.country_code)
print("Number: ", mynum.national_number)




# To check if the number is valid: phonenumbers.is_valid_number(mynum)
if phonenumbers.is_valid_number(mynum):
    print("IT IS A VALID NUMBER")
else:
    print("IT IS AN INVALID NUMBER")




# geocode.description_for_number(): To know which country does the number belong to
# 2 arguments: the parsed number, the language
location = geocoder.description_for_number(mynum, "en")
print("This number belongs to", location.upper())




# carrier.name_for_number(mynum): Returns the carrier to which the number belongs to
service_provider = carrier.name_for_number(mynum, "en")
print(service_provider, "is its service provider.")


# Printing the location of the number: 
# Happens using aother library called opencage. (Not required for this project)


