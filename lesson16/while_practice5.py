email = input("Enter your email address: ")

n = 0
count = 0

while n < len(email):
    if email[n] == "@":
        count += 1
    n += 1

print(count)