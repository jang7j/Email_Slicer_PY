#collect email from user
#split the email using @ --first part will be username, second part will be domain
#split domain using . --first part will be domain, second part will be extension

def main():
    print("")
    print("--Welcome to Email Slicer--")

    email_input = input("Input your email address: ") 

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

while True:
    main()

