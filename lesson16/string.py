string = input("Enter a string of at least 5 characters: ")
if len(string) < 5:
    print("The string is too short.")
else:
    string = string[3:]
    print(string)
    string = string.replace(' ', '-')
    print(string)