import re


def check_first_name():
    while True:
        first_name=input("enter the first name : ")
        name_pattern=r"^[A-Z][a-z]{2,}$"
        if re.match(name_pattern,first_name):
            return first_name
        else:
            print("error: enter the correct value")

def check_last_name():
    while True:
        last_name=input("enter the last name : ")
        name_pattern=r"^[A-Z][a-z]{2,}$"
        if re.match(name_pattern,last_name):
            return last_name
        else:
            print("error: enter the correct value")

def check_email():
    while True:
        e_mail=input("enter the mail : ")
        mail_pattern=r"^[a-zA-Z0-9.+_-]+@[a-z0-9-]+(\.[a-zA-Z]{2,})+$"
        if re.match(mail_pattern,e_mail):
            return e_mail
        else:
            print("error: enter the correct email")
       
def main():
    first_name = check_first_name()
    last_name = check_last_name()
    e_mail=check_email()
    print(f"Valid First Name :{first_name}")
    print(f"valid last name :{last_name}")
    print(f"valid e_mail :{e_mail}")


if __name__=='__main__':
    main()
   

    
    
    