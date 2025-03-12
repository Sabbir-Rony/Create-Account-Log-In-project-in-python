print("Create Account Now")
username = input("Enter Username: ")
passward = input("Enter Passward: ")

print("Your account has been create successfully")
print("LogIn Now")

username2 = input("Enter Username: ")
passward2 = input("Enter Passward: ")

if username == username2 and passward == passward2:
    print("Logged In Successfully")
else:
    print("Invalid Credentials")
