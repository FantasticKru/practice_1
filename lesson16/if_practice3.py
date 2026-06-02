email = input("Enter your email address: ")
if len(email) < 4 or email[0] == "@" or email[-1] == "@":
    print("ERROR")