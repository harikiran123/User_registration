first_name =str(input("enter the first name : "))
if len(first_name) > 3:
    if first_name[0].isupper():
        print(f"enter user name is true: {first_name}")
    else:
        print("enter a valid user name")
else:
    print("enter a valid user name")
    