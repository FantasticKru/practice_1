string = input("Enter a string")
len_string = len(string)
if len_string < 4:
    print("too short")
elif len_string > 9:
    print("too long")
elif 4 <= len_string <= 9:
    print("ok")