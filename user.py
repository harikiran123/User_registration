import re

def check_email():

    '''
    Description: This function validates whether the given email address is in the correct format.
    - Contains alphanumeric characters, dots, underscores, plus, or hyphens before '@'
    - Contains a domain name with at least one dot
     - Ends with a valid top-level domain (TLD)
    Parameters: None
    Return: None 
    '''

    e_mail = input("Enter the email: ")
    e_mail_pattern = r"^[a-zA-Z0-9.+_-]+@[a-z0-9-]+(\.[a-zA-Z]{2,})+$"
    
    if re.fullmatch(e_mail_pattern, e_mail):
        print("Valid email")
    else:
        print("Invalid email")

def main():
    check_email()


if __name__ == '__main__':
    main()
