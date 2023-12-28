#Take input from user
#split input email by '@' and store each part in a variable
#take second part of initial split and split by '.' and store each part in a variable
#print the username, domain_name and extention to the console

def main():

    email = input("Enter an email address: ")
    (username, domain) = email.split("@")

    (domain_name, extension) = domain.split(".")

    print("Username is: ",username)
    print("Domain name is: ",domain_name)
    print("Extension is: ",extension)

while True:
    main()