from getpass import getpass

username = input("Enter Your Username: ")
password = getpass("Enter Your Password: ")

if username == "Koosha" and password == "maktab78":
    print("Login Successfully.")
else:
    print("Username or Password Wrong.")

print('Changed by Ali')

if True:
    print(False)