import re
e_mail=input("enter the email : ")
e_mail_pattern=r"^[a-zA-Z0-9.+_-]+@[a-z0-9-]+(\.[a-zA-Z]{2,})+$"
if re.fullmatch(e_mail_pattern,e_mail):
    print("valid email")
else:
    print("invalid")