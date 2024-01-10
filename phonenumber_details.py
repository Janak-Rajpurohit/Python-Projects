from time import timezone
import phonenumbers  as pn
from phonenumbers import timezone ,geocoder,carrier

def check_valid(number):
    if pn.is_valid_number(number):        ## IF NUMBER IS VALID then it will call DETAIL function which PRINTS DETAILS
        timezone,car,region,=details(number)   ## returns time_zone  carrier and region

        print(f"Time zone --> {timezone}") 
        print(f"Carrier --> {car}")
        print(f"Region --> {region}")

    else:
        print("You Phone number is not valid.")         ## else print message
        print("Please enter correct mobile number.")

def details(number):
    ## gives time zone of the number
    tz=timezone.time_zones_for_number(number) 
    #find carrier 
    c=carrier.name_for_number(number,"en")
    #find region
    region=geocoder.description_for_number(number,'en')
    return tz,c,region


if  __name__=="__main__":
    n=input("Enter phone number >>> ")
    number=pn.parse(n)
    print(number)
    check_valid(number)
    
"""__MORE  FUNCTIONS__"""
# text =" contact me on +918976380287 and +114562783."
# numbers=pn.PhoneNumberMatcher(text,"IN")       # extract phonenumber from text
# for i in numbers:
#     print(i)

# possible=pn.is_possible_number(number)       ## can number be a phone number (if it contain right no of digits)
# print(possible)