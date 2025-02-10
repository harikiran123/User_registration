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






first_name = get_first_name()
last_name = get_last_name()
e_mail=get_email()





print(f"Entered first name '{first_name}' is valid.")
print(f"Entered last name '{last_name} is valid")
print(f"enteted email {e_mail} is valid")