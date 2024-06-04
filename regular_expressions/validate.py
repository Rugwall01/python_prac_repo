# Validating email addresses 
email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
    



username, domain = email.split("@")


if username and "." in domain:
    print("Valid")
else:
    print("Invalid")




    
username, domain = email.split("@")


if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")



#This all gets complicated fast, thepython library called re library lets us have a library for regular expressions capabilities to define check for and replace patterns
# Defining these patterns and validate input against these patterns, extract partial input from or change input from user
