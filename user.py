import re


def check_first_name():
    while True:
        first_name=input("enter the first name : ")
        name_pattern=r"^[A-Z][a-z]{2,}$"
        if re.match(name_pattern,first_name):
            return first_name
        else:
            print("error: enter the correct value")
   


if __name__=='__main__':
    first_name = check_first_name()
    print(f"Valid First Name:{first_name}")

    
    

    