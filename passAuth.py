import getpass


database={"degraft":"silver","frimpong":"1234"}
username=input("Enter username :")
password=getpass.getpass("Enter password :")

for i in database.keys():
    if username==i:
        while password != database.get(i):
            password=getpass.getpass("Enter your password again ")
        break
print("User is verified!")