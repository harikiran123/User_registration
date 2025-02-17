import re


def check_first_name():

    '''
    Description: This function will check if the given first_name is in the correct format or not.
    Parameters: None
    Return: first_name
    '''

    while True:
        first_name=input("enter the first name : ")
        name_pattern=r"^[A-Z][a-z]{2,}$"
        if re.match(name_pattern,first_name):
            return first_name
        else:
            print("error: enter the correct value")

def check_last_name():

    '''
    Description: This function will check if the given last_name is in the correct format or not.
    Parameters: None
    Return: last_name
    '''

    while True:
        last_name=input("enter the last name : ")
        name_pattern=r"^[A-Z][a-z]{2,}$"
        if re.match(name_pattern,last_name):
            return last_name
        else:
            print("error: enter the correct value")
        
def main():

    '''
    Description: This function calls check_first_name and check_last_name functions and prints valid names.
    Parameters: None
    Return: None
    '''
    
    first_name = check_first_name()
    last_name = check_last_name()
    print(f"Valid First Name :{first_name}")
    print(f"valid last name :{last_name}")


if __name__=='__main__':
    main()
   

    
    
    