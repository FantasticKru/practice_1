age = input("Enter your age: ")
if age < 0:
    age = 0
elif age > 120:
    age = 120
elif 0 <= age <= 18:
    print("teenager")
elif 19 <= age <= 120:
    print("adult")