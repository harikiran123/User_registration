import re

def get_first_name():
    while True:
        f_name = input("Enter the first name: ")
        
        if len(f_name) > 2:  
            if f_name[0].isupper():  
                return f_name  
            else:
                print("Error: First name must start with an uppercase letter.")
        else:
            print("Error: First name must contain at least 3 letters.")


def get_last_name():
    while True:
        l_name= input("enter the last name : ")
        if len(l_name) > 2:
            if l_name[0].isupper():
                return l_name
            else:
                print("error: last name must start with an uppercase letter ")
        else:
            print("error: last name must contain at least 3 letters")

def get_email():

    while True:
        e_mail=input("enter the email: ")
        mail_patteren = r"^[a-zA-Z0-9/.+-_]+@gmail\.com$"
        if re.match(mail_patteren,e_mail):
            return e_mail
        else:
            print("error: enter the cotterct email formate")

def get_country_code():
    while True:
        country_code=input("enter the country code : ")
        if country_code.isdigit():
            return country_code
        else:
            print("error:country code should be in interger value ")
def get_mobile_number():
    while True:
        mobile_number=input("enter the moblie number")
        if len(mobile_number) == 10:
            if mobile_number.isdigit():
                return mobile_number
            else:
                print("error:mobile number must be in integer")
        else:
            print("error: the mobile number should be in 10 digits")
            
def get_password():
    
    while True:
        password= input("enter the password: ")
        if len(password) > 7:
            if re.search(r"[A-Z]",password):
                if re.search(r"[0-9]",password):
                    if re.search(r'[/.+\-_!@#$%^&*()]', password):
                        return password
                    else:
                        print("error: password must contain atlest one special char")
                else:
                    print("error: password must contain atleast one numeric value")
            else:
                print("error: passwor must contain atleast one upper case")
        else:
            print("error:password should caontain min 8 characters")
            
        


first_name = get_first_name()
last_name = get_last_name()
e_mail=get_email()
country_code=get_country_code()
mobile_number=get_mobile_number()
password=get_password()




print(f"Entered first name '{first_name}' is valid.")
print(f"Entered last name '{last_name} is valid")
print(f"enteted email {e_mail} is valid")
print(f"entered mobile number '{country_code} {mobile_number}'is valid")
print(f"entered password {password} is valid")