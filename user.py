first_name =str(input("enter the first name : "))
last_name=str(input("enter the last name : "))
if len(first_name) > 3 and len(last_name) > 3:
    if first_name[0].isupper() and last_name[0].isupper():
        print(f"entered  first name '{first_name}' is true")
        print(f"entered last name '{last_name}' is true")
    else:
        print("enter a valid user name")
else:
    print("enter a valid user name")
