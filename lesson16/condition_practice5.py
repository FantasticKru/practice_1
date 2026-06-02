password = input("Enter a password: ")
len_password = len(password)
if len_password < 8:
    print("too short")
elif password[0] not in ["Z", "C"]:
    print("must start with Z or C")
elif password[-1] not in ["$"]:
    print("must end with $")
else: 
    print("STRONG PASSWORD")
